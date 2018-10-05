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
      )
    b-field(
      horizontal
      label='use ssl?'
    )
      b-switch(
        type='is-primary'
      ) ff
</template>

<script>
// imports
import store from '@/store/store'
// helpers
const genComputed = key => ({
  get () {
    const remote = store.getters.remote(this.remoteID)
    return remote.config[key]
  },
  set (value) {
    store.commit('updateRemoteConfig', {
      remoteID: this.remoteID,
      key,
      value
    })
  }
})
// export
export default {
  props: [
    'remoteID'
  ],
  computed: {
    hostname: genComputed('hostname'),
    username: genComputed('username')
  }
}
</script>
