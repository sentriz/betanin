<template lang="pug">
  b-tabs(v-model='activeTab')
    br
    b-tab-item(label='notifications')
      notification-editor
    b-tab-item(label='beets config')
      config-editor
</template>

<script>
// imports
import ConfigEditor from '@/components/settings/ConfigEditor.vue'
import NotificationEditor from '@/components/settings/NotificationEditor.vue'
// export
export default {
  components: {
    ConfigEditor,
    NotificationEditor
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
