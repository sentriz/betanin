<template lang="pug">
  .container
    #app
      .section
          nav-bar
      .section
          router-view
    #footer
      status
      connection-banner
</template>

<script>
import ConnectionBanner from '@/components/ConnectionBanner.vue'
import NavBar from '@/components/NavBar.vue'
import Status from '@/components/Status.vue'
export default {
  name: 'activity',
  components: {
    NavBar,
    Status,
    ConnectionBanner
  }
}
</script>

<style lang="scss">
  @import "~bulma/sass/utilities/_all";
  $primary:           #d1536a;
  $primary-invert:    findColorInvert($primary);
  $green:             #23d160;
  $green-invert:      findColorInvert($green);
  $link-focus-border: $primary;
  $link-invert:       $primary-invert;
  $link:              $primary;
  $colors: (
    "primary": ($primary, $primary-invert),
    "green": ($green, $green-invert),
  );
  #app {
    min-height: 100vh;
  }
  #footer {
    position: sticky;
    left: 0;
    right: 0;
    bottom: 0;
    width: 100%;
    padding-top: 70px;
    background: linear-gradient(rgba(255, 255, 255, 0), white);
    pointer-events: none;

  }
  #connection-banner {
    margin-top: 0.4rem;
  }
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
