<template lang="pug">
  torrents(:torrents='getHistory')
    .title.is-6
      b-icon(icon='alert')
      | &nbsp; there are no imported torrents yet
</template>

<script>
import Torrents from '@/components/Torrents.vue'
import { mapGetters } from 'vuex'
export default {
  components: {
    Torrents
  },
  computed: {
    ...mapGetters('torrents', [
      'getHistory'
    ])
  }
}
</script>
