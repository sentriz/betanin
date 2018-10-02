<!-- b-icon(icon='menu-down') -->
<template lang="pug">
  div
    b-field(
      horizontal
      label='host/port'
    )
      b-input(
        placeholder='example.com'
      )
      b-input(
        v-model='port'
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
        v-model='password'
      )
    b-field(
      horizontal
      label='use ssl?'
    )
      b-switch(
        v-model='useSSL'
        type='is-primary'
      ) {{ useSSL }}
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
export default {
  data () {
    return {
      useSSL: true,
      host: '',
      port: '80',
      username: '',
      password: ''
    }
  }
}
</script>
