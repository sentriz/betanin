<template lang="pug">
  .modal-card
    header.modal-card-head
      p.modal-card-title {{ torrent(torrentID).name }}
    base-console.modal-card-body(
      :torrentID='torrentID'
    )
    footer.modal-card-foot
      #send-input
        b-input(
          @keyup.enter='sendStdin'
          size='is-small'
          type='text'
          v-bind='inputProps'
          v-model='stdin'
        )
      #send-button
        button.button.is-dark.is-small(
          @click='sendStdin'
          v-bind='inputProps'
        ) send
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
  ]
]
// export
export default {
  data () {
    return {
      stdin: ''
    }
  },
  components: {
    BaseConsole
  },
  props: [
    'torrentID'
  ],
  computed: {
    ...mapGetters([
      'torrent'
    ]),
    inputProps () {
      const { status } = this.torrent(this.torrentID)
      for (let i = 0; i < inputPropMap.length; i++) {
        const [stati, props] = inputPropMap[i]
        if (stati.includes(status)) {
          return props
        }
      }
    }
  },
  methods: {
    sendStdin (event) {
      const postUrl = `torrents/${this.torrentID}/console/stdin`
      const payload = {
        text: this.stdin
      }
      backend.postResource(postUrl, payload)
      this.stdin = ''
    }
  }
}
</script>

<style lang="scss" scoped>
  .modal-card-title {
    font-size: 1rem;
  }
  .modal-card-head, .modal-card-foot {
    padding: 0.75rem 0.75rem;
  }
  #send-row {
    display: flex;
  }
  #send-input {
    flex-grow: 1;
    margin-right: 0.75rem;
  }
  #send-button {
    flex-basis: 4rem;
    flex-shrink: 0;
    button {
      width: 100%;
    }
  }
</style>
