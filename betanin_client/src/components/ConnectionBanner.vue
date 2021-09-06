<template lang="pug">
.banner
  .disconnected(v-show='!getConnected')
    p disconnected
  .version
    p {{ getSystemInfo.betaninVersion }}
  .status
    p <b>{{ getHistoryCount }}</b> imports, {{ getActivityCount }} active
</template>

<script>
// import
import store from '@/store/main'
import { mapGetters } from 'vuex'
// export
export default {
  computed: mapGetters({
    getConnected: 'status/getConnected',
    getSystemInfo: 'status/getSystemInfo',
    getActivityCount: 'torrents/getActivityCount',
    getHistoryCount: 'torrents/getHistoryCount',
  }),
  mounted() {
    store.dispatch('status/doFetchSystemInfo')
  },
}
</script>

<style lang="scss" scoped>
@import '~bulma';
.banner {
  width: 100%;
  color: black;
  display: flex;
  justify-content: flex-end;
  > * ~ * {
    margin-left: 10px;
  }
}
.disconnected {
  border-radius: 0.5rem;
  color: white;
  display: inline-block;
  padding: 0 0.5rem;
  background-color: $danger;
}
.version {
  opacity: 0.6;
}
</style>
