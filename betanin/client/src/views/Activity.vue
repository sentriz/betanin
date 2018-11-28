<template lang="pug">
  torrents(:torrents='getActivity')
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
      'getActivity'
    ])
  }
}
</script>
