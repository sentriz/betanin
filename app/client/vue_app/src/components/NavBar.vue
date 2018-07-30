<template lang="pug">
  nav.navbar.is-transparent
    .navbar-brand
      a.navbar-item(href='https://bulma.io')
        img#logo(
          src='../assets/logo.png',
          height='23'
        )
    .navbar-menu
      .navbar-start
        router-link.navbar-item(to='/activity') Activity
        router-link.navbar-item(to='/history') History
        router-link.navbar-item(to='/settings') Settings
</template>

<style scoped>
 #logo {
    margin-right: 2.5rem;
  }
</style>
