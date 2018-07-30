<template lang="pug">
  #app
    .section
      .container
        NavBar
    .section
      .container
        router-view
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'activity',
  components: {
    NavBar
  }
}
</script>
