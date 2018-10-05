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
        a.button.is-light
          | test
      p.control
        a.button.is-primary
          | save
      p.control
        a.button.is-primary
          | delete
</template>

<script>
// imports
import confComps from '@/data/possible_remote_config_components'
import { mapGetters } from 'vuex'
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
  data () {
    return {
      remoteNames: Object.keys(confComps),
      confComps
    }
  }
}
</script>
