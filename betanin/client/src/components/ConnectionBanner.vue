<template lang="pug">
  .content.has-text-centered#connection-banner(
    :class="connected ? 'green' : 'red'"
  )
    p(
      v-if='connected'
    ) connected to backend
    p(
      v-else
    ) not connected to backend
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
  #connection-banner {
    clip-path: polygon(
      0.3rem 0,
      calc(100% - 0.3rem) 0,
      100% 100%,
      0% 100%
    );
  }
</style>
