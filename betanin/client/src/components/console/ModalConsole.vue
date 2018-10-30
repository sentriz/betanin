<template lang="pug">
  .modal-card
    header.modal-card-head
      p.modal-card-title {{ torrent(torrentID).name }}
    base-console.modal-card-body(
      :torrentID='torrentID'
      :isLive='isLive'
    )
    footer.modal-card-foot
      #send-input
        b-input(
          @keyup.enter='sendStdin'
          size='is-small'
          type='text'
          :disabled='!isLive'
          :placeholder='isLive ? "send to to beets" : "beets has quit"'
          v-model='stdin'
        )
      #send-button
        button.button.is-dark.is-small(
          @click='sendStdin'
          :disabled='!isLive'
        ) send
</template>

<script>
// imports
import BaseConsole from '@/components/console/BaseConsole.vue'
import backend from '@/backend'
import { mapGetters } from 'vuex'
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
    isLive () {
      const { status } = this.torrent(this.torrentID)
      return ['PROCESSING', 'NEEDS_INPUT'].includes(status)
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
