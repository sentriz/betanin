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
    .field.is-grouped.is-grouped-right#buttons
      p.control
        a.button(@click='testRemote').is-light
          | test
      p.control
        a.button(@click='saveRemote').is-primary
          | save
      p.control
        a.button(@click='removeRemote(remoteID)').is-primary
          | remove
</template>

<script>
// imports
import { mapGetters, mapMutations } from 'vuex'
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
      console.log('test')
    },
    saveRemote () {
      console.log('save')
    },
    ...mapMutations([
      'removeRemote'
    ])
  }
}
</script>
