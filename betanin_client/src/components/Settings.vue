<template lang="pug">
div
  nav.tabs
    ul
      router-link(to="/settings/clients", custom, v-slot='{ href, isActive }')
        li(:class="[isActive && 'is-active']")
          a(:href='href')
            b-icon(icon="download")
            | torrent clients
      router-link(to="/settings/notifications", custom, v-slot='{ href, isActive }')
        li(:class="[isActive && 'is-active']")
          a(:href='href')
            b-icon(icon="alert-circle")
            | notifications
      router-link(to="/settings/beets", custom, v-slot='{ href, isActive }')
        li(:class="[isActive && 'is-active']")
          a(:href='href')
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
