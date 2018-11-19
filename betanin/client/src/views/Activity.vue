<template lang="pug">
  torrents(:torrents='torrentsActivity')
</template>

<script>
import Torrents from '@/components/Torrents.vue'
import { mapGetters } from 'vuex'
export default {
  components: {
    Torrents
  },
  computed: {
    ...mapGetters([
      'torrentsActivity'
    ])
  }
}
</script>
