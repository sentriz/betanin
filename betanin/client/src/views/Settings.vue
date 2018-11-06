<template lang="pug">
  b-tabs(v-model='activeTab')
    br
    b-tab-item(label='general')
      p not needed yet
    b-tab-item(label='beets config')
      config-editor
</template>

<script>
// imports
import ConfigEditor from '@/components/settings/ConfigEditor.vue'
// export
export default {
  components: {
    ConfigEditor
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
