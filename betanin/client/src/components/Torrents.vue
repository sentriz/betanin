<template lang="pug">
  div
    b-table(
      :data='torrents'
      :opened-detailed='openedDetails'
      detailed
      detail-key='id'
      paginated
      :per-page='itemsPerPage'
    )
      template(slot-scope='props')
        b-table-column(label='name') {{ props.row.name | truncate(64) }}
        b-table-column(label='status' :numeric='true')
          span.status-group(:style='{ color: statusStyle(props.row.status).colour }')
            b-icon(:icon='statusStyle(props.row.status).icon' size='is-small')
            |  {{ statusStyle(props.row.status).text }}
          span.status-group.link(v-show='props.row.has_lines' @click='openModal(props.row.id)')
            b-icon(icon='console' size='is-small')
            |  view
          span.status-group(v-show='["FAILED", "COMPLETED"].includes(props.row.status)')
            span.link(title='remove torrent' @click='doDeleteOneTorrent(props.row.id)')
              b-icon.link(icon='close' size='is-small')
            | &nbsp;
            span.link(title='retry import' @click='doRetryOneTorrent(props.row.id)')
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
        slot
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
    ]),
    itemsPerPage () {
      const viewHeight = Math.max(
        document.documentElement.clientHeight,
        window.innerHeight || 0
      )
      return Math.floor(viewHeight - 370) / 44
    }
  },
  components: {
    ModalConsole
  },
  props: [
    'torrents',
    'emptyString'
  ],
  methods: {
    ...mapActions({
      doDeleteOneTorrent: 'torrents/doDeleteOne',
      doRetryOneTorrent: 'torrents/doRetryOne'
    }),
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
    word-break: break-all;
  }
  .link {
    cursor: pointer;
  }
  .status-group ~ .status-group::before {
    content: "｜";
    display: inline-block;
    margin: 0 0.1rem;
    opacity: 0.15;
  }
</style>
