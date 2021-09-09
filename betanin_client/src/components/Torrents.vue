<template lang="pug">
div
  .manual-search
    manual-import
    br
  no-active(v-if='torrents.length == 0')
  b-table.torrents(
    v-else,
    :data='torrents',
    :loading='loading',
    :opened-detailed='openedDetails',
    detailed,
    detail-key='id',
    paginated,
    backend-pagination,
    :total='getTotal',
    :per-page='perPage',
    @page-change='onPageChange'
  )
    b-table-column(label='name', v-slot='props') {{ props.row.name }}
    b-table-column(label='status', :numeric='true', v-slot='props')
      .controls
        torrent-status(:status='props.row.status')
        router-link.status-group.link(
          v-show='props.row.has_lines',
          :to='{ name: "modal console", params: { torrentID: props.row.id } }'
        )
          b-icon(icon='console', size='is-small')
          |
          | view
        span.status-group(v-if='["FAILED", "COMPLETED"].includes(props.row.status)')
          span.link(title='remove torrent', @click='deleteTorrent(props.row.id)')
            b-icon.link(icon='close', size='is-small')
          | &nbsp;
          span.link(title='retry import', @click='retryTorrent(props.row.id)')
            b-icon.link(title='retry import', icon='refresh', size='is-small')
    template(#detail='props')
      .row-status
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
import ManualImport from '@/components/ManualImport.vue'
import TorrentStatus from '@/components/TorrentStatus.vue'
import store from '@/store/main'
import backend from '@/backend'
import { TORRENTS_ALL_APPEND } from '@/store/mutation-types'
import { mapGetters } from 'vuex'

export default {
  components: {
    ManualImport,
    NoActive,
    TorrentStatus,
  },
  data() {
    return {
      page: 1,
      perPage: 25,
      torrentIDs: [],
      openedDetails: [],
      loading: false,
    }
  },
  computed: {
    ...mapGetters('torrents', ['getTorrent', 'getTotal']),
    torrents() {
      return this.torrentIDs.map((id) => this.getTorrent(id)).filter((t) => !!t)
    },
  },
  methods: {
    retryTorrent(torrentID) {
      if (!confirm('do you want to retry this?')) return
      store.dispatch('torrents/doRetryOne', torrentID)
      this.$router.push({
        name: 'modal console',
        params: { torrentID },
      })
    },
    deleteTorrent(torrentID) {
      if (!confirm('do you want to remove this from betanin?')) return
      store.dispatch('torrents/doDeleteOne', torrentID)
      this.load()
    },
    onPageChange(page) {
      this.page = page
      this.load()
    },
    async load() {
      const params = { page: this.page, per_page: this.perPage }
      const result = await backend.secureAxios.get('torrents/', { params })
      this.loading = true
      store.commit(`torrents/${TORRENTS_ALL_APPEND}`, { total: result.data.total, torrents: result.data.torrents })
      this.torrentIDs = result.data.torrents.map((t) => t.id)
      this.loading = false
    },
  },
  mounted() {
    this.load()
  },
  sockets: {
    newTorrent(torrent) {
      if (this.page !== 1 || this.getTorrent(torrent.id)) return
      this.torrentIDs.unshift(torrent.id)
    },
  },
}
</script>

<style lang="scss" scoped>
.torrents ::v-deep td {
  vertical-align: middle;
}
.link {
  cursor: pointer;
}
.controls > * + * {
  margin-left: 0.75rem;
  display: inline-block;
}
a {
  color: unset;
}
</style>
