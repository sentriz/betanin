<template lang="pug">
  .content.has-text-centered(
    v-bind:class="connected ? 'green' : 'red' "
  )
    p(
      v-if='connected'
    ) connected to backend
    p(
      v-else
    ) lost connection to backend
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  computed: mapGetters([
    'connected'
  ])
}
</script>

<style lang="scss" scoped>
  @import "~bulma";
  p {
    color: white;
  }
  .content {
    opacity: 0.8;
  }
  .red {
    background-color: $danger;
  }
  .green {
    background-color: $success;
  }
</style>
