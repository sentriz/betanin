<template lang="pug">
  #container
    #lines
      slot
    #footer
      a(
        @click="showModal"
      ) click to see full console
</template>

<script>
export default {
  props: [
    'showModal'
  ]
}
</script>

<style scoped>
#lines * {
    background-color: #fafafa;
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
