<template lang="pug">
  div
    remote(
      v-for='remoteID in remoteIDs'
      :remoteID='remoteID'
      :key='remoteID'
    )
    p.control.is-pulled-right
      a.button(
        @click='addRemote'
      ).is-primary
        | add
</template>

<script>
// imports
import Remote from '@/components/Remote.vue'
import { mapGetters, mapActions } from 'vuex'
// export
export default {
  components: {
    Remote
  },
  computed: {
    ...mapGetters([
      'remoteIDs'
    ])
  },
  methods: {
    ...mapActions([
      'addRemote'
    ])
  }
}
</script>

<style scoped>
  #buttons {
    padding-top: 12px;
  }
</style>
