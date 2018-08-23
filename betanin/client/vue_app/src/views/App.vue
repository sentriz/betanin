<template lang="pug">
  #app
    #content
      .section
        .container
          nav-bar
      .section
        .container
          router-view
    #footer
      connection-banner
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import ConnectionBanner from '@/components/ConnectionBanner.vue'
export default {
  name: 'activity',
  components: {
    NavBar,
    ConnectionBanner
  }
}
</script>

<style lang="scss">
  @import "~bulma";
  $primary:           #d1536a;
  $primary-invert:    findColorInvert($primary);
  $link-focus-border: $primary;
  $link-invert:       $primary-invert;
  $link:              $primary;
  #app {
    display: flex;
    min-height: 100vh;
    flex-direction: column;
  }
  #content {
    flex: 1;
  }
</style>
