<template lang="pug">
  div#line
    b-switch#enabled-switch(
      v-model='enabled'
    ) {{ ['no', 'yes'][Number(service.enabled)] }}
    #url
      .select
        select(
          v-model='protocol'
        )
          option(disabled value='') please select
          option(
            v-for='service in getPossibleProtocols(service.type)'
            :key='service'
            :value='service'
          ) {{ service}}
      p#protocol-helper ://
      b-input#not-protocol-box(
        icon='earth'
        placeholder='see info button for help'
        v-model='notProtocol'
      )
      a(
        :href='getPossibleInfo(service.type)'
        target='_blank'
      )
        b-icon(
          icon='information'
          type='is-info'
        )
    p.control
      button.button.left-button(@click='NOTI_SERVICE_DELETE(service.id)') remove
</template>

<script>
// imports
import { NOTI_SERVICE_UPDATE, NOTI_SERVICE_DELETE } from '@/store/mutation-types'
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
      NOTI_SERVICE_UPDATE,
      NOTI_SERVICE_DELETE
    ])
  }
}
</script>

<style lang="scss">
  #url {
    display: flex;
    align-items: center;
    > * {
      margin: 0 5px;
    }
    #not-protocol-box {
      width: 500px;
    }
    #protocol-helper {
      font-family: monospace;
    }
  }
  #line {
    padding: 0.5rem;
    background-color: #fafafa;
    border-radius: 5px;
    #enabled-switch {
      width: 35px;
    }
    margin: 0.30rem 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
</style>
