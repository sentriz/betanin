<template lang="pug">
  #container
    #lines
      base-console(
        :lineLimit='10'
        :torrentID='torrentID'
      )
    #footer
      a(
        @click='openModal'
      ) click to see full console
</template>

<script>
// imports
import BaseConsole from '@/components/console/BaseConsole.vue'
import ModalConsole from '@/components/console/ModalConsole.vue'
// export
export default {
  components: {
    BaseConsole
  },
  props: [
    'torrentID'
  ],
  methods: {
    openModal () {
      this.$modal.open({
        parent: this,
        component: ModalConsole,
        props: {
          torrentID: this.torrentID
        },
        hasModalCard: true
      })
    }
  }
}
</script>

<style scoped>
  #lines * {
    padding: 0;
    width: 100%;
    -webkit-mask-image: -webkit-gradient(
      linear,
      left bottom,
      left top,
      from(rgba(0, 0, 0, 0.65)),
      to(rgba(0, 0, 0, 0))
    );
  }
  #footer {
    padding-top: 0.75rem;
  }
</style>
