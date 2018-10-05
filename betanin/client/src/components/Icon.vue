<template lang="pug">
  span(
    v-bind:style="getStyle(appearance.colour)"
  )
    b-icon(
      :icon='appearance.icon',
      size='is-small',
    )
    |  {{ appearance.text }}
</template>

<script>
export default {
  props: [
    'appearance'
  ],
  methods: {
    getStyle (colour) {
      return {
        'color': this.appearance.colour
      }
    }
  }
}
</script>
