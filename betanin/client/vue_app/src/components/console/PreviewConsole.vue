<template lang="pug">
  #container
    pre#lines
      p(
        v-for='line in this.isPreview ? lastN(lines, 10) : lines'
      ) {{ line.index }}: {{ line.data }}
    #footer
      a(
        @click="showModal"
      ) click to see full console
</template>

<script>
export default {
  props: [
    'lines',
    'showModal',
    'isPreview'
  ],
  methods: {
    lastN (list, n) {
      return list.slice(-n)
    }
  }
}
</script>

<style scoped>
  #lines {
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
