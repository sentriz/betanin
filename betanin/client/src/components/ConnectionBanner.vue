<template lang="pug">
  #banner(
    :class="getConnected ? 'green' : 'red'"
  )
    #version
      p
        span(v-show='betaninVersion') ver.&nbsp;
        b {{ betaninVersion | truncate(8, ' ') }}
    #connection
      p(v-show='!getConnected').
        disconnected
    #status
      p.
        {{ getHistoryCount }} imports, {{ getActivityCount }} active
</template>

<script>
// import
import { mapGetters } from 'vuex'
// export
export default {
  computed: mapGetters({
    getConnected: 'status/getConnected',
    getActivityCount: 'torrents/getActivityCount',
    getHistoryCount: 'torrents/getHistoryCount'
  }),
  data () {
    return {
      // eslint-disable-next-line
      betaninVersion: __SOURCE_COMMIT__
    }
  }
}
</script>

<style lang='scss' scoped>
  @import "~bulma";
  * {
    color: white;
  }
  .red {
    background-color: $danger;
  }
  .green {
    background-color: $success;
  }
  #banner {
    z-index: 1000000;
    padding: 0 1rem;
    display: flex;
    opacity: 0.85;
    clip-path: polygon(
      0.3rem 0,
      calc(100% - 0.3rem) 0,
      100% 100%,
      0% 100%
    );
    > * {
      flex: 1;
      display: flex;
      justify-content: center;
      &:first-child > p {
        margin-right: auto;
      }
      &:last-child > p {
        margin-left: auto;
      }
    }
  }
  @media only screen and (max-width: 768px) {
    #banner {
      display: none;
    }
  }
</style>
