<template lang="pug">
  downloads(:downloads='downloadsHistory')
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
      'downloadsHistory'
    ])
  }
}
</script>
