<template lang="pug">
  .modal-card
    .box#header
      h2.subtitle {{ header }}
    .box#lines
      slot
    .box#footer
      input.input(
        type='text'
        placeholder='send text to beets'
      )
</template>

<script>
export default {
  props: [
    'header'
  ]
}
</script>

<style scoped>
  #lines * {
    height: 60vh;
    overflow-y: scroll;
    overflow-x: hidden;
  }
</style>
