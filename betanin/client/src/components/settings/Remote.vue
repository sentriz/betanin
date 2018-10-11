<template lang="pug">
  div
    b-field(
      horizontal
      label='type'
    )
      b-input(
        placeholder='transmission.com'
        :value='remoteTypeFromID(remoteID)'
        disabled
      )
    slot
    br
    b-field(grouped group-multiline position='is-right')
      p.control
        button.button(@click='testRemote').is-light test
      p.control
        button.button(@click='saveRemote(remoteID)').is-primary save
      p.control
        button.button(@click='removeRemote(remoteID)').is-primary remove
    hr
</template>

<script>
// imports
import backend from '@/backend'
import { mapGetters, mapActions } from 'vuex'
// export
export default {
  props: [
    'remoteID'
  ],
  computed: {
    ...mapGetters([
      'remoteTypeFromID'
    ])
  },
  methods: {
    testRemote () {
      const fetchUrl = `settings/remotes/${this.remoteID}/test`
      backend.fetchResource(fetchUrl)
        .then(response => {
          const type = response.ok ? 'is-success' : 'is-danger'
          const prefix = response.ok ? 'succeeded' : 'failed'
          this.$toast.open({
            message: `testing ${prefix}: ${response.reason}`,
            type
          })
        })
    },
    ...mapActions([
      'removeRemote',
      'saveRemote'
    ])
  }
}
</script>

<style scoped>
  .control {
    margin-bottom: 0 !important;
  }
</style>
