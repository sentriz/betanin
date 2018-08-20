<template lang="pug">
  pre
    p(
      v-for='line in lines'
    ) {{ line.data }}
</template>

<script>
export default {
  props: ['lines'],
  methods: {}
}
</script>
