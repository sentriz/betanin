<template lang="pug">
  pre
    p(
      v-for='line in lines(torrentID, lineLimit)'
      :key='line.index'
    ) {{ line.data }}
</template>

<script>
// imports
import { mapGetters, mapActions, mapMutations } from 'vuex'
// export
export default {
  props: [
    'lineLimit',
    'torrentID'
  ],
  computed: mapGetters([
    'lines',
    'linesFetched'
  ]),
  methods: {
    ...mapActions([
      'getLines'
    ]),
    ...mapMutations([
      'markLinesFetched'
    ])
  },
  mounted () {
    if (!this.linesFetched(this.torrentID)) {
      this.getLines(this.torrentID)
      this.markLinesFetched(this.torrentID)
    }
  }
}
</script>

<style scoped>
  pre {
    background-color: #404040;
    padding: 0.75rem;
    height: 50vh;
  }
  p {
    font-size: 11px;
    color: white;
  }
</style>
