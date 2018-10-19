<template lang="pug">
  pre
    p(
      v-for='line in lines(torrentID, lineLimit)'
      :key='line.index'
    ) {{ line.data }}
</template>

<script>
// imports
import { mapGetters } from 'vuex'
// export
export default {
  props: [
    'lineLimit',
    'torrentID'
  ],
  computed: mapGetters([
    'lines'
  ])
}
</script>

<style scoped>
  pre {
    background-color: initial;
  }
  p {
    font-size: 12px;
  }
</style>
