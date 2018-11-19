<template lang="pug">
  torrents(:torrents='torrentsHistory')
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
      'torrentsHistory'
    ])
  }
}
</script>
