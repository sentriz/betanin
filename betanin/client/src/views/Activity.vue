<template lang="pug">
  downloads(:downloads='downloadsActivity')
</template>

<script>
import Downloads from '@/components/Downloads.vue'
import { mapGetters } from 'vuex'
export default {
  components: {
    Downloads
  },
  computed: {
    ...mapGetters([
      'downloadsActivity'
    ])
  }
}
</script>
