<template lang="pug">
  div
    component(
      :is='emptyTorrentsComponent'
      v-if='torrents.length == 0'
    )
    b-table(
      v-else
      :data='torrents'
      :opened-detailed='openedDetails'
      detailed
      detail-key='id'
      paginated
      :per-page='itemsPerPage'
      :pagination-simple='true'
    )
      template(slot-scope='props')
        b-table-column(label='name') {{ props.row.name | truncate(64) }}
        b-table-column(label='status' :numeric='true')
          span.status-group(:style='{ color: statusStyle(props.row.status).colour }')
            b-icon(:icon='statusStyle(props.row.status).icon' size='is-small')
            |  {{ statusStyle(props.row.status).text }}
          router-link.status-group.link(
            v-show='props.row.has_lines'
            :to=`{ name: 'modal console', params: { torrentID: props.row.id } }`
          )
            b-icon(icon='console' size='is-small')
            |  view
          span.status-group(v-show='["FAILED", "COMPLETED"].includes(props.row.status)')
            span.link(title='remove torrent' @click='deleteTorrent(props.row.id)')
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
    router-view(name='modal')
</template>

<script>
// imports
import NoActive from '@/components/tips/NoActive.vue'
import NoHistory from '@/components/tips/NoHistory.vue'
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
    ...mapGetters('torrents', [
      'getActivity',
      'getHistory'
    ]),
    itemsPerPage () {
      const viewHeight = window.innerHeight || 0
      const perPage = Math.floor(viewHeight - 370) / 44
      return Math.round(perPage)
    },
    emptyTorrentsComponent () {
      return this.$route.params.listType === 'active'
        ? NoActive
        : NoHistory
    },
    torrents () {
      return this.$route.params.listType === 'active'
        ? this.getActivity
        : this.getHistory
    }
  },
  // mounted () {
  //   // force table header
  //   Vue.set(this.$children[0], 'data',
  //     [{ status: 'COMPLETED', name: '_' }])
  // },
  methods: {
    ...mapActions({
      doDeleteOneTorrent: 'torrents/doDeleteOne',
      doRetryOneTorrent: 'torrents/doRetryOne'
    }),
    retryTorrent (torrentID) {
      if (confirm('do you want to retry this?')) {
        this.doRetryOneTorrent(torrentID)
        this.$router.push({
          name: 'modal console', params: { torrentID }
        })
      }
    },
    deleteTorrent (torrentID) {
      if (confirm('do you want to remove this from betanin?')) {
        this.doDeleteOneTorrent(torrentID)
      }
    },
    statusStyle (status) {
      return statusMap[status]
    }
  },
  data () {
    return {
      openedDetails: []
    }
  }
}
</script>

<style scoped>
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
  a {
    color: unset;
  }
</style>
