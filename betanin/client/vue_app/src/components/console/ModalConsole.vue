<template lang="pug">
  .modal-card
    .box#header
      h2.subtitle {{ torrent(torrentID).name }}
    .box#lines
      base-console(
        :torrentID='torrentID'
      )
    .box#footer
      input.input(
        type='text'
        @keyup.enter='sendStdin'
        v-bind='getInputProps()'
      )
</template>

<script>
// imports
import BaseConsole from '@/components/console/BaseConsole.vue'
import backend from '@/backend'
import { mapGetters } from 'vuex'
// help
const inputPropMap = [
  [
    ['PROCESSING', 'NEEDS_INPUT'], {
      disabled: false,
      placeholder: 'send text to beets'
    }
  ], [
    ['COMPLETED', 'FAILED'], {
      disabled: true,
      placeholder: 'beets has quit'
    }
  ], [
    ['WAITING'], {
      disabled: true,
      placeholder: 'waiting for beets to start'
    }
  ]
]
// export
export default {
  components: {
    BaseConsole
  },
  props: [
    'torrentID'
  ],
  computed: mapGetters([
    'torrent'
  ]),
  methods: {
    sendStdin (event) {
      const postUrl = 'torrents/' + this.torrentID + '/console/stdin'
      const payload = {
        text: event.target.value
      }
      backend.postResource(postUrl, payload)
    },
    getInputProps () {
      const status = this.torrent(this.torrentID).beta_status
      for (let i = 0; i < inputPropMap.length; i++) {
        const [stati, props] = inputPropMap[i]
        if (stati.includes(status)) {
          return props
        }
      }
    }
  }
}
</script>

<style scoped>
  #lines * {
    height: 60vh;
    overflow-y: scroll;
    overflow-x: hidden;
  }
</style>
