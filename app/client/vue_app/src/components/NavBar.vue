<template lang="pug">
  nav.navbar.is-transparent
    .navbar-brand
      a.navbar-item(href='https://bulma.io')
        img(
          src='https://bulma.io/images/bulma-logo.png',
          alt='Bulma: a modern CSS framework based on Flexbox',
          width='112',
          height='28'
        )
    #mainNav.navbar-menu
      .navbar-start
        router-link.navbar-item(to='/activity') Activity
        router-link.navbar-item(to='/history') History
        router-link.navbar-item(to='/settings') Settings
</template>
