<template lang="pug">
  pre
    #live-box(v-show='isLive')
      span#live-fade &#x26AB
      span#live-text live
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
    'torrentID',
    'isLive'
  ],
  computed: mapGetters([
    'lines',
    'linesFetched',
    'torrent'
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
    position: relative;
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
    color: white;
    font-size: 14px;
    word-spacing:  3px;
    padding: 0 0.5rem;
    padding-top: 0.3rem;
    border-radius: 2px;
    background-color: rgba(255, 255, 255, 0.1);
  }
  #live-fade {
    color: red;
    animation: fadeinout 2s;
    animation-iteration-count: infinite;
    margin-right: 4px;
  }
</style>
