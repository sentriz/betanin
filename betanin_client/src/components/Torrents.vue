<template lang="pug">
  div
    #manual-search(v-show='isActivity()')
      manual-import
      br
    component(
      :is='emptyTorrentsComponent'
      v-if='torrents.length == 0'
    )
    b-table#torrents(
      v-else
      :data='torrents'
      :opened-detailed='openedDetails'
      detailed
      detail-key='id'
      paginated
      per-page='50'
      :pagination-simple='true'
    )
      template(slot-scope='props')
        b-table-column(label='name') {{ props.row.name }}
        b-table-column.controls(label='status' :numeric='true')
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
            <strong>id</strong> {{ props.row.id }}
          p
            <strong>status</strong> {{ props.row.status | lower }}
          p
            <strong>created</strong> {{ props.row.created }}
          p
            <strong>updated</strong> {{ props.row.updated }}
    router-view(name='modal')
</template>

<script>
// imports
import NoActive from '@/components/tips/NoActive.vue'
import NoHistory from '@/components/tips/NoHistory.vue'
import ManualImport from '@/components/ManualImport.vue'
import store from '@/store/main'

// help
const statusMap = {
  /* eslint-disable no-multi-spaces, key-spacing, standard/object-curly-even-spacing */
  'ENQUEUED':    { text: 'enqueued',    icon: 'clock-outline', colour: 'hsl(36, 99%, 65%)'  }, // orange
  'PROCESSING':  { text: 'processing',  icon: 'clock-fast',    colour: 'hsl(48, 98%, 52%'   }, // yellow
  'NEEDS_INPUT': { text: 'needs input', icon: 'alert',         colour: 'hsl(48, 98%, 52%)'  }, // yellow-orange
  'FAILED':      { text: 'failed',      icon: 'close',         colour: 'hsl(349, 58%, 57%)' }, // angry red
  'COMPLETED':   { text: 'completed',   icon: 'check',         colour: 'hsl(141, 71%, 48%)' }  // green
}
// export
export default {
  components: {
    ManualImport
  },
  computed: {
    emptyTorrentsComponent () {
      return this.isActivity()
        ? NoActive
        : NoHistory
    },
    torrents () {
      return this.isActivity()
        ? store.getters['torrents/getActivity']
        : store.getters['torrents/getHistory']
    }
  },
  methods: {
    isActivity () {
      return this.$route.params.listType === 'active'
    },
    retryTorrent (torrentID) {
      if (confirm('do you want to retry this?')) {
        store.dispatch('torrents/doRetryOne', torrentID)
        this.$router.push({
          name: 'modal console', params: { torrentID }
        })
      }
    },
    deleteTorrent (torrentID) {
      if (confirm('do you want to remove this from betanin?')) {
        store.dispatch('torrents/doDeleteOne', torrentID)
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
  },
  mounted () {
    store.dispatch('torrents/doFetchAll')
  }
}
</script>

<style lang='scss' scoped>
  #torrents /deep/ td {
    vertical-align: middle;
  }
  #row-status {
    text-align: right;
    word-break: break-all;
  }
  .link {
    cursor: pointer;
  }
  .status-group ~ .status-group::before {
    content: '\00a0';
    display: inline-block;
    margin: 0 0.1rem;
    opacity: 0.15;
  }
  .controls {
    white-space: nowrap;
  }
  a {
    color: unset;
  }
</style>
