<template lang="pug">
  pre#lines
    p(
      v-for='line in this.isPreview ? lastN(lines, 10) : lines'
    ) {{ line.index }}: {{ line.data }}
</template>

<script>
export default {
  props: [
    'lines',
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
    -webkit-mask-image: -webkit-gradient(
      linear,
      left bottom,
      left top,
      from(rgba(0, 0, 0, 0.65)),
      to(rgba(0, 0, 0, 0))
    );
  }
  pre {
    padding: 0;
    background-color: #fafafa;
  }
</style>
