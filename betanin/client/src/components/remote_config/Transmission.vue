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
    ssl:      genComputed('ssl')
  }
}
</script>
