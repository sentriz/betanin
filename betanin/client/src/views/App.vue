<template lang="pug">
  .container
    #app
      .section
        nav-bar
      .section
        router-view
    #footer
      .section
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
    margin: 0;
    margin-bottom: 3.5rem;
  }
  #footer {
    position: fixed;
    bottom: 0;
    left: auto;
    pointer-events: none;
    width: inherit;
    background: linear-gradient(
      rgba(255, 255, 255, 0),
      white,
      white,
    );
    @media only screen and (max-width: 1087px) {
      width: 100%;
    }
    .section {
      padding-bottom: 0;
    }
  }
  #connection-banner {
    margin-top: 0.4rem;
  }
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
