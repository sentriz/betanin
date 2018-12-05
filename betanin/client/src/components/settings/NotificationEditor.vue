<template lang="pug">
  div
    h5.title.is-5 notification format
    #general-editor
      #general-inputs
        b-field(label='title')
          b-input(v-model='generalTitle')
        b-field(label='body')
          b-input(
            placeholder='Success'
            type='textarea'
            v-model='generalBody'
          )
      #variables-help
        label.label available variables
        ul
          li
            code $id
            |  the unique id or hash of the torrent
          li
            code $title
            |  the title of the torrent
          li
            code $time
            |  the timestamp of the last update to the torrent
          li
            code $status
            |  the current betanin status of the torrent. eg. '
            b needs input
            | '
    .field.is-pulled-right.controls
      button.button.is-primary.is-right#format-save-button(@click='doPutGeneral()') save
    hr
    h5.title.is-5 services
    h6(v-show='getServices.length === 0')
      b-icon(icon='alert')
      | &nbsp; no services here yet, add one below
    notification-service(
      v-for='service in getServices'
      :serviceID='service.id'
      :key='service.id'
    )
    #service-controls.controls
      .field.has-addons#service-type-selector
        .control
          .select.is-fullwidth
            select(v-model='newServiceType')
              option(
                v-for='service in getPossible'
                :key='service.service_name'
                :value='service.service_name'
              ) {{ service.service_name }}
        .control
          button.button(@click='doPostService(newServiceType)') add new
      .field
        .field
          .control
            button.button.is-primary(
              @click='doPutServices()'
              :class='{ "is-loading": getIsTesting }'
            ) save
</template>

<script>
// imports
import NotificationService from '@/components/settings/NotificationService.vue'
import { genNotiGeneralComputed } from '@/utilities'
import { mapActions, mapGetters } from 'vuex'
// export
export default {
  components: {
    NotificationService
  },
  created () {
    this.doFetchPossible()
    this.doFetchServices()
    this.doFetchGeneral()
  },
  computed: {
    ...mapGetters('notifications', [
      'getServices',
      'getPossible',
      'getIsTesting'
    ]),
    generalTitle: genNotiGeneralComputed('title'),
    generalBody: genNotiGeneralComputed('body')
  },
  methods: {
    ...mapActions('notifications', [
      'doFetchPossible',
      'doFetchServices',
      'doFetchGeneral',
      'doPutGeneral',
      'doPostService',
      'doPutServices'
    ])
  },
  data () {
    return {
      newServiceType: 'Kodi/XBMC'
    }
  }
}
</script>

<style lang="scss" scoped>
  hr {
    margin-top: 5rem;
  }
  .controls {
    margin-top: 24px;
  }
  #general-save-button {
    margin-top: 24px;
  }
  #general-editor {
    width: 100%;
    display: flex;
    align-items: stretch;
    #variables-help {
      margin-left: 2rem;
      @media only screen and (max-width: 768px) {
        display: none;
      }
    }
    > * {
      flex: 1 100%;
    }
  }
  #service-controls {
    display: flex;
    justify-content: flex-end;
    #service-type-selector {
      margin-right: 1rem;
    }
  }
  #general-inputs /deep/ textarea {
    min-height: calc(36px * 2);
    max-height: unset;
  }
</style>
