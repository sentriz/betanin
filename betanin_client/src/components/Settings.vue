<template lang="pug">
div
  nav.tabs
    ul
      //- b-tabs doesnt't support router, so try make it match
      //- also using:
      //- https://router.vuejs.org/api/#applying-active-class-to-outer-element
      router-link(tag="li", to="/settings/clients")
        a
          b-icon(icon="download")
          | torrent clients
      router-link(tag="li", to="/settings/notifications")
        a
          b-icon(icon="alert-circle")
          | notifications
      router-link(tag="li", to="/settings/beets")
        a
          b-icon(icon="note")
          | beets config
  router-view
</template>

<style lang="scss" scoped>
::v-deep {
  .tab-item {
    margin-top: 2rem;
  }
  .tab-content {
    padding: 0 !important;
  }
}
</style>
