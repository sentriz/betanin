<template lang="pug">
  b-tabs(v-model='activeTab')
    b-tab-item(label='general')
      .section
        b-field(horizontal label='local directory')
          b-input(icon='folder' placeholder='~/media/music')
    b-tab-item(label='torrent clients')
      .section
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

<style scoped>
</style>
