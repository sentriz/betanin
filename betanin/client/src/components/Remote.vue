    <!-- .field.is-grouped.is-grouped-right#buttons -->
<template lang="pug">
  .box
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
    b-field(grouped group-multiline position='is-right')
      p.control
        button.button(@click='testRemote').is-light test
      p.control
        button.button(@click='saveRemote(remoteID)').is-primary save
      p.control
        button.button(@click='removeRemote(remoteID)').is-primary remove
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
          const type = response.ok
            ? 'is-success'
            : 'is-danger'
          const prefix = response.ok
            ? 'testing succeeded'
            : 'testing failed'
          this.$toast.open({
            message: `${prefix}: ${response.reason}`,
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
