'
<template lang="pug">
#line
  b-switch#enabled-switch(v-model='enabled') {{ ["disabled", "enabled"][Number(service.enabled)] }}
  #url
    validation-provider(name='protocol', rules='required', v-slot='{ errors }')
      b-field(:type='{ "is-primary": errors.length }', :message='errors[0]')
        b-select#protocol-selector(v-model='protocol')
          option(disabled, value='') please select
          option(v-for='service in getPossibleProtocols(service.type)', :key='service', :value='service') {{ service }}
    p#protocol-helper ://
    validation-provider(name='notProtocol', rules='required', v-slot='{ errors }')
      b-field(:type='{ "is-primary": errors.length }', :message='errors[0]')
        b-input#not-protocol-box(icon='earth', placeholder='see info button for help', v-model='notProtocol')
    a#info-link(:href='getPossibleInfo(service.type)', target='_blank')
      b-icon(icon='information', type='is-info')
  p#delete-button.control
    button.button.left-button(@click='NOTI_SERVICE_DELETE(service.id)') remove
</template>

<script>
// imports
import { ValidationProvider } from 'vee-validate'
import { NOTI_SERVICE_DELETE } from '@/store/mutation-types'
import { mapMutations, mapGetters } from 'vuex'
import store from '@/store/main'
import { genNotiServiceComputed } from '@/utilities'
// export
export default {
  components: {
    ValidationProvider,
  },
  props: ['serviceID'],
  data() {
    return {
      deleteIsVisible: false,
    }
  },
  computed: {
    ...mapGetters('notifications', ['getPossibleProtocols', 'getPossibleInfo']),
    service() {
      const services = store.getters['notifications/getServiceByID']
      return services[this.serviceID]
    },
    enabled: genNotiServiceComputed('enabled'),
    protocol: genNotiServiceComputed('protocol'),
    notProtocol: genNotiServiceComputed('not_protocol'),
  },
  methods: {
    ...mapMutations('notifications', [NOTI_SERVICE_DELETE]),
  },
}
</script>

<style lang="scss" scoped>
#url {
  display: flex;
  align-items: flex-start;
  > * {
    margin: 0 5px;
  }
  ::v-deep #not-protocol-box {
    width: 500px;
  }
  #protocol-helper {
    font-family: monospace;
  }
}
#line {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  background-color: #fafafa;
  border-radius: 5px;
  padding: 0.5rem;
  margin: 0.5rem 0;
}
#protocol-helper,
#info-link,
#delete-button,
#enabled-switch {
  height: 40px;
  line-height: 40px;
}
</style>
