<template lang="pug">
  pre
    #live-box(v-show='isLive')
      span#live-fade &#x25A0
      span#live-text live
    p(
      v-for='line in getAllLines(torrentID, lineLimit)'
      :key='line.index'
      v-html='colorLine(line.data)'
    )
</template>

<script>
// imports
import { LINES_FETCHED_CREATE } from '@/store/mutation-types'
import { mapGetters, mapActions, mapMutations } from 'vuex'
// help
const Convert = require('ansi-to-html')
const converter = new Convert()
// export
export default {
  props: [
    'lineLimit',
    'torrentID',
    'isLive'
  ],
  computed: {
    ...mapGetters({
      getAllLines: 'lines/getAll',
      getFetchedLines: 'lines/getFetched'
    }),
    ...mapGetters({
      getOneTorrent: 'torrents/getOne'
    })
  },
  methods: {
    ...mapActions({
      doFetchAllLines: 'lines/doFetchAll'
    }),
    ...mapMutations({
      [LINES_FETCHED_CREATE]: `lines/${LINES_FETCHED_CREATE}`
    }),
    colorLine (line) {
      return converter.toHtml(line)
    }
  },
  mounted () {
    if (!this.getFetchedLines(this.torrentID)) {
      this.doFetchAllLines(this.torrentID)
      this[LINES_FETCHED_CREATE](this.torrentID)
    }
  }
}
</script>

<style scoped>
  pre {
    background-color: #404040;
    padding: 0.75rem;
    height: 50vh;
    position: relative;
    overflow-x: hidden;
  }
  p {
    font-size: 11px;
    color: white;
  }
  @keyframes fadeinout {
    0%, 60%, 100% {opacity: 1;}
    80%           {opacity: 0;}
  }
  #live-box {
    position: absolute;
    top: 0px;
    right: 0px;
    margin: 0.75rem;
    font-size: 14px;
    word-spacing:  3px;
    padding: 0 0.5rem;
    border-radius: 2px;
    background-color: rgba(255, 255, 255, 0.1);
  }
  #live-fade {
    color: red;
    animation: fadeinout 2s;
    animation-iteration-count: infinite;
    margin-right: 4px;
    font-size: 18px;
  }
  #live-text {
    color: white;
  }
</style>
