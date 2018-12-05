<template lang="pug">
  torrents(:torrents='getActivity')
    h6.title.is-6
      b-icon(icon='alert')
      | &nbsp; there are no torrents being imported at the moment
    .title.is-7
      | make sure that you have set your torrent client up correctly
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
