<template lang="pug">
  div
    b-table(:data='torrents'
            :opened-detailed='openedDetails'
            detailed
            detail-key='id')
      template(slot-scope='props')
        b-table-column(label='name') {{ props.row.name | truncate(64) }}
        b-table-column(label='status' :numeric='true')
          span(:style='{ color: statusStyle(props.row.status).colour }')
            b-icon(:icon='statusStyle(props.row.status).icon' size='is-small')
            |  {{ statusStyle(props.row.status).text }}
          span.sepe &nbsp;&nbsp;|&nbsp;&nbsp;
          span.link(v-show='props.row.has_lines' @click='openModal(props.row.id)')
            b-icon(icon='console' size='is-small')
            |  view
          span(v-show='["FAILED", "COMPLETED"].includes(props.row.status)')
            span.sepe &nbsp;&nbsp;|&nbsp;&nbsp;
            span.link(title='remove torrent' @click='removeTorrent(props.row.id)')
              b-icon.link(icon='close' size='is-small')
            | &nbsp;
            span.link(title='retry import' @click='retryTorrent(props.row.id)')
              b-icon.link(title='retry import' icon='loop' size='is-small')
      template(slot-scope='props'
               slot='detail')
        #row-status
          p
            strong id
            |  {{ props.row.id }}
          p
            strong status
            |  {{ props.row.status | lower }}
          p
            strong created
            |  {{ props.row.created }}
          p
            strong updated
            |  {{ props.row.updated }}
      template(slot='empty')
        h6(v-show='torrents.length === 0')
          b-icon(icon='alert')
          | &nbsp; no torrents here yet, check the status below
    b-modal(
      :width='640'
      scroll='keep'
      :active.sync='modalIsOpen'
    )
      modal-console(
        :torrentID='modalTorrentID'
      )
</template>

<script>
// imports
import ModalConsole from '@/components/console/ModalConsole.vue'
import Vue from 'vue'
import { mapGetters, mapActions } from 'vuex'
// help
const statusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  'ENQUEUED': { text: 'enqueued', icon: 'clock-outline', colour: 'hsl(36, 99%, 65%)' }, // orange
  'PROCESSING': { text: 'processing', icon: 'clock-fast', colour: 'hsl(48, 98%, 52%' }, // yellow
  'NEEDS_INPUT': { text: 'needs input', icon: 'alert', colour: 'hsl(48, 98%, 52%)' }, // yellow-orange
  'FAILED': { text: 'failed', icon: 'close', colour: 'hsl(349, 58%, 57%)' }, // angry red
  'COMPLETED': { text: 'completed', icon: 'check', colour: 'hsl(141, 71%, 48%)' }, // green
  'DOWNLOADING': { text: 'downloading', icon: 'sleep', colour: 'hsl(0, 0%, 86%)' } // light grey
}
// export
export default {
  computed: {
    ...mapGetters([
      'activeModal',
      'areLines',
      'lines'
    ])
  },
  components: {
    ModalConsole
  },
  props: [
    'torrents'
  ],
  methods: {
    ...mapActions([
      'getLines',
      'removeTorrent',
      'retryTorrent'
    ]),
    statusStyle (status) {
      return statusMap[status]
    },
    openModal (torrentID) {
      Vue.set(this, 'modalTorrentID', torrentID)
      Vue.set(this, 'modalIsOpen', true)
    }
  },
  data () {
    return {
      openedDetails: [],
      modalIsOpen: false,
      modalTorrentID: ''
    }
  }
}
</script>

<style>
  .level {
    padding-bottom: 0;
  }
  #row-status {
    text-align: right;
  }
  .sepe {
    opacity: 0.2;
  }
  .link {
    cursor: pointer;
  }
</style>
