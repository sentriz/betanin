<template lang="pug">
  #app
    .section
      .container
        NavBar
    .section
      .container
        router-view
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'activity',
  components: {
    NavBar
  }
}
</script>

<style lang="scss">
  @import "~bulma/sass/utilities/_all";

  $primary: #d1536a;
  $primary-invert: findColorInvert($primary);

  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  @import "~bulma";
</style>
