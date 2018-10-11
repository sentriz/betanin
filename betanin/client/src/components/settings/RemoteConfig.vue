<template lang="pug">
  div
    remote(
      v-for='remoteID in remoteIDs'
      :remoteID='remoteID'
      :key='remoteID'
    )
      component(
        :is='confFromID(remoteID)'
        :remoteID='remoteID'
      )
    h6(
      v-show='remoteIDs.length === 0'
    ) no remotes yet, add one below
    .field.has-addons.is-pulled-right
      .control
        .select.is-fullwidth
          select(
            v-model='newRemoteType'
          )
            option(
              v-for='remoteName in remoteNames'
              :key='remoteName'
              :value='remoteName'
              @click='addRemote(remoteName)'
            ) {{ remoteName }}
      .control
        button.button(
          @click='addRemote(newRemoteType)'
        ) add new
</template>

<script>
// imports
import Remote from '@/components/Remote.vue'
import confComps from '@/data/possible_remote_config_components'
import { mapGetters, mapActions } from 'vuex'
// export
export default {
  components: {
    Remote
  },
  computed: {
    ...mapGetters([
      'remoteIDs',
      'remoteTypeFromID'
    ])
  },
  methods: {
    ...mapActions([
      'addRemote'
    ]),
    confFromID (id) {
      return confComps[this.remoteTypeFromID(id)]
    }
  },
  data () {
    return {
      remoteNames: Object.keys(confComps),
      newRemoteType: 'transmission'
    }
  }
}
</script>

<style scoped>
  #buttons {
    padding-top: 12px;
  }
</style>
