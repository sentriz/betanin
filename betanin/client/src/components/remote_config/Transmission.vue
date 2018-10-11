<template lang="pug">
  div
    b-field(horizontal label='host/port')
      b-input(icon='server' placeholder='transmission.com'
              v-model='hostname')
      b-input(icon='reorder' placeholder='80' v-model='port')
    b-field(horizontal label='use ssl')
      b-switch(type='is-primary' v-model='ssl') {{ ssl | toYesNo }}
    b-field(horizontal label='path')
      b-input(icon='folder' placeholder='/transmission/rpc'
              v-model='path')
    b-field(horizontal label='login')
      b-input(icon='user' placeholder='username' v-model='username')
      b-input(icon='lock' placeholder='password' type='password'
              v-model='password' password-reveal)
    b-field(horizontal label='local map' :message='remoteMapping')
      b-input(icon='arrows-h' placeholder='/mnt/media/downloads/music'
              v-model='watchDir')
</template>

<script>
// imports
import { genComputed } from '@/utilities'
// export
export default {
  props: [
    'remoteID'
  ],
  computed: {
    /* eslint-disable key-spacing */
    hostname: genComputed('hostname'),
    path:     genComputed('path'),
    port:     genComputed('port'),
    username: genComputed('username'),
    password: genComputed('password'),
    ssl:      genComputed('ssl'),
    watchDir: genComputed('watchDir')
  },
  data () {
    return {
      remoteMapping: ''
    }
  },
  watch: {
    watchDir () {
      this.updateRemoteMapping()
    }
  },
  mounted () {
    this.updateRemoteMapping()
  },
  methods: {
    updateRemoteMapping () {
      const exampleRemoteDir = '/mnt/downloads/music'
      const exampleTorrent = 'The Fall - Dragnet'
      this.remoteMapping = this.watchDir
        ? `<b>${exampleRemoteDir}/${exampleTorrent}</b> on transmission
          would be imported from <b>${this.watchDir}/${exampleTorrent}</b> locally`
        : 'assuming betanin and transmission are on the same machine'
    }
  }
}
</script>
