<template lang="pug">
  nav.navbar
    .navbar-brand
      router-link.navbar-item(to='/')
        img#logo(
          :src='getLogoPath()'
          height='100%'
        )
      a.navbar-burger(
        role='button',
        @click='toggleShow',
        v-bind:class="{ 'is-active' : show }"
      )
        span
        span
        span
    .navbar-menu(:class="{ 'is-active': show }")
      .navbar-end
        router-link.navbar-item(to='/torrents/active') Activity
        router-link.navbar-item(to='/torrents/complete') History
        router-link.navbar-item(to='/settings') Settings
</template>

<script>
export default {
  data () {
    return {
      show: false
    }
  },
  methods: {
    toggleShow () {
      this.show = !this.show
    },
    getLogoPath () {
      // eslint-disable-next-line
      return __NODE_ENV__ === 'production'
        ? require('../assets/logo.png')
        : require('../assets/logo_dev.png')
    }
  }
}
</script>

<style scoped>
  #logo {
     margin-right: 2.5rem;
  }
  .is-active {
    font-weight: 600;
  }
</style>
