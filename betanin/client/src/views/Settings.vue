<template lang="pug">
  div
    remote(
      v-for='remoteID in remoteIDs'
      :remoteID='remoteID'
      :key='remoteID'
    )
    p.control
      a.button.is-primary
        | add
</template>

<script>
// imports
import Remote from '@/components/Remote.vue'
import { mapGetters } from 'vuex'
// export
export default {
  components: {
    Remote
  },
  computed: {
    ...mapGetters([
      'remoteIDs'
    ])
  }
}
</script>

<style scoped>
  #buttons {
    padding-top: 12px;
  }
</style>
