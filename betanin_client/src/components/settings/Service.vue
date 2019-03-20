<template lang="pug">
  div
    p hello
    br
    b-field(grouped group-multiline position='is-right')
      p.control
        button.button(@click='testService').is-light test
      p.control
        button.button(@click='removeService(serviceID)').is-primary remove
</template>

<script>
// imports
import backend from '@/backend'
import { mapGetters, mapActions } from 'vuex'
// export
export default {
  props: [
    'serviceIndex'
  ],
  methods: {
    async testService () {
      const fetchUrl = `settings/services/${this.serviceID}/test`
      const response = await backend.secureAxios.get(fetchUrl)
      const type = response.data.ok ? 'is-green' : 'is-primary'
      const prefix = response.data.ok ? 'succeeded' : 'failed'
      this.$toast.open({
        message: `testing ${prefix}: ${response.data.reason}`,
        type
      })
    },
    ...mapActions([
      'removeService'
    ])
  }
}
</script>

<style scoped>
  .control {
    margin-bottom: 0 !important;
  }
</style>
