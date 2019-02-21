<template lang="pug">
  b-tabs(v-model='activeTab' :animated='false')
    b-tab-item.tab-item(icon='download' label='torrent clients')
      torrent-clients
    b-tab-item.tab-item(icon='alert-circle' label='notifications')
      notification-editor
    b-tab-item.tab-item(icon='note' label='beets config')
      config-editor
</template>

<script>
// imports
import ConfigEditor from '@/components/settings/ConfigEditor.vue'
import NotificationEditor from '@/components/settings/NotificationEditor.vue'
import TorrentClients from '@/components/settings/TorrentClients.vue'
// export
export default {
  components: {
    ConfigEditor,
    NotificationEditor,
    TorrentClients
  },
  data () {
    return {
      activeTab: 0
    }
  }
}
</script>

<style lang='scss' scoped>
  /deep/ {
    .tab-item {
      margin-top: 2rem;
    }
    .tab-content {
      padding: 0 !important;
    }
  }
</style>
