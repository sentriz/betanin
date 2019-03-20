<template lang="pug">
  pre(v-chat-scroll)
    #live-box(v-show='isLive')
      span#live-fade &#x25A0
      span#live-text live
    p(
      v-for='line in getByID[torrentID]'
      :key='line.index'
      v-html='colorLine(line.data)'
    )
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
  props: [
    'torrentID',
    'isLive'
  ],
  computed: {
    ...mapGetters('lines', [
      'getByID'
    ])
  },
  methods: {
    colorLine (line) {
      return converter.toHtml(line)
    }
  },
  mounted () {
    store.dispatch('lines/doFetchAll', this.torrentID)
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
