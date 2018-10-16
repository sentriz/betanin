<template lang="pug">
  div
    remote(v-for='remoteID in remoteIDs'
           :remoteID='remoteID'
           :key='remoteID')
      component(:is='confFromID(remoteID)'
                :remoteID='remoteID')
    h6(v-show='remoteIDs.length === 0')
      b-icon(icon='exclamation-triangle')
      | &nbsp; no remotes yet, add one below
    .field.has-addons.is-pulled-right
      .control
        .select.is-fullwidth
          select(v-model='newRemoteType')
            option(v-for='remoteName in remoteNames'
                   :key='remoteName'
                   :value='remoteName'
                   @click='addRemote(remoteName)') {{ remoteName }}
      .control
        button.button(@click='addRemote(newRemoteType)') add new
    br
    br
    #empty-sep(v-show='remoteIDs.length === 0')
      hr
    #help.content
      h5.title.is-5 notes on transmission
      ul
        li.
          if your transmission client is running on a different to betanin,
          you need to mount the folder transmission uses locally. maybe something
          like curlftpfs, sshfs, samba, etc. then use the 'local map' field.
          start typing in it to what the mapping will look like.
        li.
          at the moment, betanin will only attempt to download torrents in the
          'category' specified. this is to prevent betanin from trying to import
          films, etc. transmission doesn't actually support categories, so you must
          choose a directory as a category. eg /default/download/dir/music, where
          'music' is the category. this setup is made easy with a browser extension
          that supports custom download directories. eg. 'transmission easy client`
          for chrome.
</template>

<script>
// imports
import Remote from '@/components/settings/Remote.vue'
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
