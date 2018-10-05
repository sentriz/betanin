<template lang="pug">
  .box
    b-field(
      horizontal
      label='type'
    )
      b-select(
        v-model='remote.type'
      )
        option(
          v-for='remoteName in remoteNames'
          :value='remoteName'
          :key='remoteName'
        ) {{ remoteName }}
    component(
      :is='confComp'
      :remoteID='remoteID'
    )
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
import confComps from '@/data/possible_remote_config_components'
import { mapGetters, mapMutations } from 'vuex'
// export
export default {
  props: [
    'remoteID'
  ],
  computed: {
    ...mapGetters({
      getRemote: 'remote'
    }),
    remote () {
      return this.getRemote(this.remoteID)
    },
    confComp () {
      return confComps[this.remote.type]
    }
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
  },
  data () {
    return {
      remoteNames: Object.keys(confComps),
      confComps
    }
  }
}
</script>
