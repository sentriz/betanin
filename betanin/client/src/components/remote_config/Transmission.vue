<template lang="pug">
  div
    b-field(
      horizontal
      label='host/port'
    )
      b-input(
        placeholder='transmission.com'
        v-model='hostname'
      )
      b-input(
        placeholder='80'
        v-model='port'
      )
    b-field(
      horizontal
      label='username/password'
    )
      b-input(
        placeholder='admin'
        v-model='username'
      )
      b-input(
        type='password'
        v-model='password'
        password-reveal
      )
    b-field(
      horizontal
      label='use ssl?'
    )
      b-switch(
        type='is-primary'
        v-model='ssl'
      ) {{ ssl | toYesNo }}
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
    port:     genComputed('port'),
    username: genComputed('username'),
    password: genComputed('password'),
    ssl:      genComputed('ssl')
  }
}
</script>
