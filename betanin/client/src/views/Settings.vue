<!-- b-icon(icon='menu-down') -->
<template lang="pug">
  .box#form
    b-field(
      horizontal
      label='remote'
    )
      b-dropdown(hoverable)
        button.button.is-info(slot='trigger')
          span {{ remote }}
        b-dropdown-item(
          v-for='remote in remotes'
          :key='remote'
          @click='setRemote(remote)'
        ) {{ remote }}
    b-field(
      horizontal
      label='host/port'
    )
      b-input(
        placeholder='example.com'
        expanded
      )
      b-input(
        placeholder='443'
        expanded
      )
    b-field(
      horizontal
      label='username/password'
    )
      b-input(
        placeholder='sam'
        expanded
      )
      b-input(
        placeholder='eggs 🤠'
        type='password'
        expanded
      )
    b-field(
      horizontal
      label='use ssl?'
    )
      b-switch(
        v-model='useSSL'
        true-value='Yes'
        false-value='No'
      )
</template>

<script>
const defaultRemote = 'transmission'
export default {
  methods: {
    setRemote (remote) {
      this.remote = remote
    }
  },
  data () {
    return {
      useSSL: false,
      remote: defaultRemote,
      remotes: [
        defaultRemote,
        'deluge',
        'rtorrent'
      ]
    }
  }
}
</script>

<style scoped>
  #form {
    padding-right: 12%;
  }
</style>
