<template lang="pug">
  nav.navbar.is-transparent
    .navbar-brand
      a.navbar-item(href='https://bulma.io')
        img#logo(
          src='../assets/logo.png',
          height='23'
        )
      a.navbar-burger(
        role='button',
        v-on:click='toggleShow()',
        v-bind:class="{ 'is-active' : show }"
      )
        span
        span
        span
    .navbar-menu(:class="{ 'is-active': show }")
      .navbar-end
        router-link.navbar-item(to='/activity') Activity
        router-link.navbar-item(to='/history') History
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
