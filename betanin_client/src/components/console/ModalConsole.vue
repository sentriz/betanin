<template lang="pug">
  b-modal(
    :width='640'
    scroll='keep'
    :active='$route.meta.modalIsOpen'
    :onCancel='openModalClose'
  )
    .modal-card
      header.modal-card-head
        p.modal-card-title {{ torrent.name }}
      base-console.modal-card-body(
        :torrentID='torrentID'
        :isLive='isLive'
      )
      footer.modal-card-foot
        #send-input
          input.input.is-small(
            @keyup.enter='sendStdin'
            type='text'
            :disabled='!isLive'
            :placeholder='isLive ? "send to beets" : "beets has quit"'
            v-model='stdin'
          )
        #send-button
          button.button.is-small(
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
  computed: {
    ...mapGetters('torrents', [
      'getOne'
    ]),
    torrentID () {
      return this.$route.params.torrentID
    },
    torrent () {
      return this.getOne(this.torrentID) || {}
    },
    isLive () {
      const { status } = this.torrent
      return ['PROCESSING', 'NEEDS_INPUT'].includes(status)
    }
  },
  methods: {
    openModalClose () {
      // not using .go(-1) here just in case there is no history
      this.$router.push({
        name: 'torrents',
        params: { listType: this.$route.params.listType }
      })
    },
    sendStdin (event) {
      backend.secureAxios.post(
        `torrents/${this.torrentID}/console/stdin`, {
          text: this.stdin
        })
      this.stdin = ''
    }
  }
}
</script>

<style lang='scss' scoped>
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
