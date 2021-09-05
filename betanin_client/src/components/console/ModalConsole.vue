<template lang="pug">
b-modal(
  :width="640",
  scroll="keep",
  :active="$route.meta.modalIsOpen",
  :onCancel="openModalClose"
)
  .modal-card
    header.modal-card-head
      p.modal-card-title {{ torrent.name }}
    #console
      base-console.modal-card-body(:torrentID="torrentID", :isLive="isLive")
      #live-box(v-show="isLive")
        span#fade &#x25A0
        span#text live
    footer.modal-card-foot
      #send-input
        input.input.is-small(
          @keyup.enter="sendStdin",
          type="text",
          :disabled="!isLive",
          :placeholder="isLive ? 'send to beets' : 'beets has quit'",
          v-model="stdin",
          v-focus
        )
      #send-button
        button.button.is-small(@click="sendStdin", :disabled="!isLive") send
</template>

<script>
// imports
import BaseConsole from "@/components/console/BaseConsole.vue";
import backend from "@/backend";
import store from "@/store/main";
// export
export default {
  data() {
    return {
      stdin: "",
    };
  },
  components: {
    BaseConsole,
  },
  computed: {
    torrentID() {
      return this.$route.params.torrentID;
    },
    torrent() {
      const torrents = store.getters["torrents/getByID"];
      return torrents[this.torrentID] || {};
    },
    isLive() {
      const { status } = this.torrent;
      return ["PROCESSING", "NEEDS_INPUT"].includes(status);
    },
  },
  methods: {
    openModalClose() {
      // not using .go(-1) here just in case there is no history
      this.$router.push({
        name: "torrents",
      });
    },
    sendStdin(event) {
      backend.secureAxios.post(`torrents/${this.torrentID}/console/stdin`, {
        text: this.stdin,
      });
      this.stdin = "";
    },
  },
  directives: {
    focus: {
      inserted(el) {
        el.focus();
      },
    },
  },
};
</script>

<style lang="scss" scoped>
.modal-card-title {
  font-size: 1rem;
}
.modal-card-head,
.modal-card-foot {
  padding: 0.75rem 0.75rem;
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
#console {
  position: relative;
}
#live-box {
  position: absolute;
  top: 0px;
  right: 0px;
  /* scrollbar is 17px */
  margin: 0.75rem calc(0.75rem + 17px);
  font-size: 14px;
  font-family: monospace;
  padding: 0 0.5rem;
  border-radius: 2px;
  background-color: rgba(255, 255, 255, 0.1);
  #fade {
    color: red;
    animation: fadeinout 2s;
    animation-iteration-count: infinite;
    margin-right: 4px;
    font-size: 18px;
  }
  #text {
    color: white;
  }
}
@keyframes fadeinout {
  0%,
  60%,
  100% {
    opacity: 1;
  }
  80% {
    opacity: 0;
  }
}
</style>
