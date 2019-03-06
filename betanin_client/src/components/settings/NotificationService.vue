<template lang="pug">
  div#line
    b-switch#enabled-switch(
      v-model='enabled'
    ) {{ ['disabled', 'enabled'][Number(service.enabled)] }}
    #url
      b-field(
        :type='{"is-primary": errors.has("protocol")}'
        :message='errors.first("protocol")'
      )
         b-select#protocol-selector(
           v-model='protocol'
           v-validate="'required'"
           data-vv-name='protocol'
         )
           option(disabled value='') please select
           option(
             v-for='service in getPossibleProtocols(service.type)'
             :key='service'
             :value='service'
           ) {{ service}}
      p#protocol-helper ://
      b-field(
        :type='{"is-primary": errors.has("notProtocol")}'
        :message='errors.first("notProtocol")'
      )
        b-input#not-protocol-box(
          icon='earth'
          placeholder='see info button for help'
          v-model='notProtocol'
          v-validate="'required'"
          data-vv-name='notProtocol'
        )
      a#info-link(
        :href='getPossibleInfo(service.type)'
        target='_blank'
      )
        b-icon(
          icon='information'
          type='is-info'
        )
    p.control#delete-button
      button.button.left-button(
        @click='NOTI_SERVICE_DELETE(service.id)'
      ) remove
</template>

<script>
// imports
import { NOTI_SERVICE_DELETE } from '@/store/mutation-types'
import { mapMutations, mapGetters } from 'vuex'
import { genNotiServiceComputed } from '@/utilities'
// export
export default {
  props: [
    'serviceID'
  ],
  data () {
    return {
      deleteIsVisible: false
    }
  },
  computed: {
    ...mapGetters('notifications', [
      'getServiceFromID',
      'getPossibleProtocols',
      'getPossibleInfo'
    ]),
    service () {
      return this.getServiceFromID(this.serviceID)
    },
    enabled: genNotiServiceComputed('enabled'),
    protocol: genNotiServiceComputed('protocol'),
    notProtocol: genNotiServiceComputed('not_protocol')
  },
  methods: {
    ...mapMutations('notifications', [
      NOTI_SERVICE_DELETE
    ])
  }
}
</script>

<style lang='scss' scoped>
  #url {
    display: flex;
    align-items: flex-start;
    > * {
      margin: 0 5px;
    }
    /deep/ #not-protocol-box {
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
  #protocol-helper, #info-link, #delete-button, #enabled-switch {
    height: 36px;
    line-height: 36px;
  }
</style>
