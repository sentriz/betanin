<template lang="pug">
  b-tabs(v-model='activeTab' :animated='false')
    b-tab-item.tab-item(icon='alert-circle-outline' label='notifications')
      notification-editor
    b-tab-item.tab-item(icon='note-outline' label='beets config')
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

<style lang="scss" scoped>
  /deep/ {
    .tab-item {
      margin-top: 2rem;
    }
    .tab-content {
      padding: 0 !important;
    }
  }
</style>
