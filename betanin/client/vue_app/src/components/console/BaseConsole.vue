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
    'torrentID',
    'lineLimit'
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
</style>
