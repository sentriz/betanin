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
  computed: {
    ...mapGetters([
      'serviceFromIndex'
    ])
  },
  methods: {
    testService () {
      const fetchUrl = `settings/services/${this.serviceID}/test`
      backend.fetchResource(fetchUrl)
        .then(response => {
          const type = response.ok ? 'is-green' : 'is-primary'
          const prefix = response.ok ? 'succeeded' : 'failed'
          this.$toast.open({
            message: `testing ${prefix}: ${response.reason}`,
            type
          })
        })
    },
    ...mapActions([
      'removeService',
      'saveService'
    ])
  }
}
</script>

<style scoped>
  .control {
    margin-bottom: 0 !important;
  }
</style>
