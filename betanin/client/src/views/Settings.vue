<template lang="pug">
  b-tabs(v-model='activeTab')
    br
    b-tab-item(label='general')
      p not needed yet
    b-tab-item(label='torrent clients')
      remote-config
</template>

<script>
// imports
import RemoteConfig from '@/components/settings/RemoteConfig.vue'
// export
export default {
  components: {
    RemoteConfig
  },
  data () {
    return {
      activeTab: 0
    }
  }
}
</script>

<style>
  .tab-content {
    padding: 0 !important;
  }
</style>
