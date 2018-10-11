<template lang="pug">
  div
    b-field(horizontal label='host/port')
      b-input(icon='globe' placeholder='transmission.com'
              v-model='hostname')
      b-input(icon='server' placeholder='80' v-model='port')
    b-field(horizontal label='use ssl')
      b-switch(type='is-primary' v-model='ssl') {{ ssl | toYesNo }}
    b-field(horizontal label='path')
      b-input(icon='folder' placeholder='/transmission/rpc'
              v-model='path')
    b-field(horizontal label='login')
      b-input(icon='user' placeholder='username' v-model='username')
      b-input(icon='lock' placeholder='password' type='password'
              v-model='password' password-reveal)
    b-field(horizontal label='category')
      b-input(icon='folder' placeholder='/downloads/complete/music'
              v-model='category')
    b-field(horizontal label='local map' :message='remoteMapping')
      b-input(icon='arrows-h' placeholder='/mnt/media/downloads/music'
              v-model='watchDir')
</template>

<script>
// imports
import { genComputed } from '@/utilities'
// help
const exampleRemoteDir = '/example/dir/music'
const exampleTorrent = 'The Fall - Dragnet'
const [winSep, unixSep] = ['\\', '/']
const cleanPath = path =>
  path.replace(/(\\|\/)+$/, '')
const isWindows = path => {
  if (!path) return false
  return path.substr(1, 2) === ':\\'
}
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
    category: genComputed('category'),
    watchDir: genComputed('watchDir'),
    remoteMapping () {
      const remoteDir = this.category
        ? this.category : exampleRemoteDir
      const localSeperator = isWindows(this.watchDir)
        ? winSep : unixSep
      const remoteSeperator = isWindows(this.category)
        ? winSep : unixSep
      return this.watchDir
        ? `if <b>${cleanPath(remoteDir)}${remoteSeperator}${exampleTorrent}</b> was downloaded
          on the transmission machine, we would try to import
          <b>${cleanPath(this.watchDir)}${localSeperator}${exampleTorrent}</b> locally`
        : 'assuming betanin and transmission are on the same machine'
    }
  }
}
</script>
