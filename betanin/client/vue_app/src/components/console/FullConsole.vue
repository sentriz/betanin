<template lang="pug">
  .modal-card
    pre#lines
      p(
        v-for='line in lines'
      ) {{ line.index }}: {{ line.data }}
</template>

<script>
export default {
  props: [
    'lines'
  ]
}
</script>

<style scoped>
</style>
