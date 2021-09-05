<template lang="pug">
pre(v-chat-scroll)
  p(v-for='line in getByID[torrentID]', :key='line.index', v-html='colorLine(line.data)')
</template>

<script>
// imports
import store from '@/store/main'
import { mapGetters } from 'vuex'
// help
import Convert from 'ansi-to-html'
const converter = new Convert()
// export
export default {
  props: ['torrentID', 'isLive'],
  computed: {
    ...mapGetters('lines', ['getByID']),
  },
  methods: {
    colorLine(line) {
      return converter.toHtml(line)
    },
  },
  mounted() {
    store.dispatch('lines/doFetchAll', this.torrentID)
  },
}
</script>

<style scoped>
pre {
  background-color: #404040;
  padding: 0.75rem;
  height: 50vh;
  position: relative;
  overflow-y: scroll;
}
p {
  font-size: 11px;
  color: white;
}
</style>
