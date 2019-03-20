<template lang="pug">
  div
    h5.title.is-5 notification format
    #strings-editor
      #strings-inputs
        b-field(label='title')
          b-input(v-model='stringsTitle')
        b-field(label='body')
          b-input(
            type='textarea'
            v-model='stringsBody'
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
          li
            code $console_path
            |  the relative path to the console modal
    .field.is-pulled-right.controls
      button.button.is-primary.is-right#format-save-button(
        @click='doPutStrings()'
      ) save
    hr
    h5.title.is-5 services
    #service-editor
      h6(v-show='getServices.length === 0')
        b-icon(icon='alert')
        | &nbsp; no services here yet, add one below
      notification-service(
        v-for='service in getServices'
        :serviceID='service.id'
        :key='service.id'
        ref='services'
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
                @click='saveServices()'
                :class='{ "is-loading": getIsTesting }'
              ) save
</template>

<script>
// imports
import NotificationService from '@/components/settings/NotificationService.vue'
import { ValidationObserver } from 'vee-validate'
import { genNotiStringsComputed } from '@/utilities'
import { mapActions, mapGetters } from 'vuex'
import store from '@/store/main'
// export
export default {
  components: {
    NotificationService,
    ValidationObserver
  },
  mounted () {
    store.dispatch('notifications/doFetchPossible')
    store.dispatch('notifications/doFetchServices')
    store.dispatch('notifications/doFetchStrings')
  },
  computed: {
    ...mapGetters('notifications', [
      'getServices',
      'getPossible',
      'getIsTesting'
    ]),
    stringsTitle: genNotiStringsComputed('title'),
    stringsBody: genNotiStringsComputed('body')
  },
  methods: {
    ...mapActions('notifications', [
      'doPutStrings',
      'doPostService',
      'doPutServices'
    ]),
    async saveServices () {
      const services = this.$refs.services || []
      const promises = services.map(service =>
        service.$validator.validateAll())
      const results = await Promise.all(promises)
      if (results.every(v => v)) {
        this.doPutServices()
      }
    }
  },
  data () {
    return {
      newServiceType: 'Kodi/XBMC'
    }
  }
}
</script>

<style lang='scss' scoped>
  hr {
    margin-top: 5rem;
  }
  .controls {
    margin-top: 24px;
  }
  #strings-save-button {
    margin-top: 24px;
  }
  #strings-editor {
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
  #strings-inputs /deep/ {
    textarea, input {
      padding: 5px;
    }
    textarea {
      min-height: calc(36px * 2);
      max-height: unset;
    }
  }
</style>
