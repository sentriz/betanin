<template lang="pug">
div
  h5.title.is-5 notification format
  #strings-editor
    #strings-inputs
      b-field(label='title')
        b-input(v-model='stringsTitle')
      b-field(label='body')
        b-input(type='textarea', v-model='stringsBody')
    #variables-help
      label.label available variables
      ul
        li <code>$id</code> the unique id or hash of the torrent
        li <code>$title</code> the title of the torrent
        li <code>$time</code> the timestamp of the last update to the torrent
        li <code>$status</code> the current betanin status of the torrent. eg. '<b>needs input</b>'
        li <code>$console_path</code> the relative path to the console modal
  .field.is-pulled-right.controls
    button#format-save-button.button.is-primary.is-right(@click='doPutStrings()') save
  hr
  h5.title.is-5 services
  validation-observer#service-editor(v-slot='{ handleSubmit }')
    h6(v-show='getServices.length === 0')
      b-icon(icon='alert')
      | &nbsp; no services here yet, add one below
    notification-service(v-for='service in getServices', :serviceID='service.id', :key='service.id')
    #service-controls.controls
      #service-type-selector.field.has-addons
        .control
          .select.is-fullwidth
            select(v-model='newServiceType')
              option(v-for='service in getPossible', :key='service.service_name', :value='service.service_name') {{ service.service_name }}
        .control
          button.button(@click='doPostService(newServiceType)') add new
      .field
        .field
          .control
            button.button.is-primary(@click='handleSubmit(doPutServices)', :class='{ "is-loading": getIsTesting }') save
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
    ValidationObserver,
  },
  mounted() {
    store.dispatch('notifications/doFetchPossible')
    store.dispatch('notifications/doFetchServices')
    store.dispatch('notifications/doFetchStrings')
  },
  computed: {
    ...mapGetters('notifications', ['getServices', 'getPossible', 'getIsTesting']),
    stringsTitle: genNotiStringsComputed('title'),
    stringsBody: genNotiStringsComputed('body'),
  },
  methods: {
    ...mapActions('notifications', ['doPutStrings', 'doPostService', 'doPutServices']),
  },
  data() {
    return {
      newServiceType: 'Kodi/XBMC',
    }
  },
}
</script>

<style lang="scss" scoped>
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
#strings-inputs ::v-deep {
  textarea,
  input {
    padding: 5px;
  }
  textarea {
    min-height: calc(36px * 2);
    max-height: unset;
  }
}
</style>
