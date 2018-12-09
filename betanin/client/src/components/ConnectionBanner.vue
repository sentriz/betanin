<template lang="pug">
  #banner(
    :class="getConnected ? 'green' : 'red'"
  )
    .side-item#version
      span(v-show='betaninVersion') ver.&nbsp;
      b {{ betaninVersion | truncate(8, ' ') }}
    #connection
      p(v-if='getConnected') connected to backend
      p(v-else) not connected to backend
    .side-item#status
      p {{ getHistoryCount }} imports, {{ getActivityCount }} active
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
    z-index: 10000;
    padding: 0 1rem;
    display: flex;
    flex-flow: row wrap;
    justify-content: space-between;
    opacity: 0.85;
    clip-path: polygon(
      0.3rem 0,
      calc(100% - 0.3rem) 0,
      100% 100%,
      0% 100%
    );
    > * {
      width: 33.33%;
    }
    #version {
      text-align: left;
    }
    #connection {
      text-align: center;
    }
    #status {
      text-align: right;
    }
    @media only screen and (max-width: 768px) {
      .side-item {
        display: none;
      }
      #connection {
        width: 100%;
      }
    }
  }
</style>
