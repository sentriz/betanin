<template lang="pug">
  .container
    #app
      .main-section
        nav-bar
      .main-section
        router-view
    #footer
      .main-section
        connection-banner
</template>

<script>
import ConnectionBanner from '@/components/ConnectionBanner.vue'
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'activity',
  components: {
    NavBar,
    ConnectionBanner
  }
}
</script>

<style lang='scss'>
  @import "~bulma/sass/utilities/_all";
  $primary:           #d1536a;
  $primary-invert:    findColorInvert($primary);
  $info:              #1f94ff;
  $info-invert:       findColorInvert($info);
  $green:             #23d160;
  $green-invert:      findColorInvert($green);
  $link-focus-border: $primary;
  $link-invert:       $primary-invert;
  $link:              $primary;
  $colors: (
    "primary": ($primary, $primary-invert),
    "green": ($green, $green-invert),
    "info": ($info, $info-invert),
  );
  #app {
    margin: 0;
  }
  .main-section {
    margin: 2rem;
  }
  #footer {
    position: fixed;
    bottom: 0;
    left: auto;
    pointer-events: none;
    width: inherit;
    @media only screen and (max-width: 1087px) {
      width: 100%;
    }
    .main-section {
      margin-bottom: 0;
    }
  }
  @import "~bulma";
  @import "~buefy/src/scss/buefy";
</style>
