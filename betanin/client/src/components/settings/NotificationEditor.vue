<template lang="pug">
  div
    b-table(:data='notificationSettingsServices')
      template(slot-scope='props')
        b-table-column(
          label='enabled'
        )
          b-field.switch-field
            b-switch(
              v-model='props.row.enabled'
              @input=`updateService({
                serviceID: props.row.id,
                key: "enabled",
                value: $event
              })`
            ) {{ ['no', 'yes'][Number(props.row.enabled)] }}
        b-table-column(label='url')
          b-field
            p.control
              b-input(
                icon='earth'
                placeholder='eggs'
                v-model='props.row.url'
                @input=`updateService({
                  serviceID: props.row.id,
                  key: "url",
                  value: $event
                })`
              )
        b-table-column
          b-field(grouped group-multiline position='is-right')
            p.control
              button.button(@click='saveNotificationSettingsService(props.row.id)').is-light save
            p.control
              button.button(@click='testService(props.row.id)').is-light test
            p.control
              button.button(@click='removeNotificationSettingsService(props.row.id)').is-primary remove
      template(slot='footer')
        .field.has-addons.is-pulled-right
          .control
            .select.is-fullwidth
              select(v-model='newServiceType')
                option(
                  v-for='service in notificationSettingsPossibleServices'
                  :key='service.service_name'
                  :value='service.service_name'
                ) {{ service.service_name }}
          .control
            button.button(@click='addNotificationSettingsService(newServiceType)') add new
      template(slot='empty')
        h6(v-show='notificationSettingsServices.length === 0')
          b-icon(icon='alert')
          | &nbsp; no services here yet, add one below

    #empty-sep(v-show='notificationSettingsServices.length === 0')
      hr
    #help.content
      h5.title.is-5 notes on transmission
      ul
        li.
          if your transmission client is running on a different to machine betanin,
          you need to mount the folder transmission uses locally. maybe something
          like curlftpfs, sshfs, samba, etc. then use the 'local map' field.
          start typing in it to what the mapping will look like.
        li.
          at the moment, betanin will only attempt to download torrents in the
          'category' specified. this is to prevent betanin from trying to import
          films, etc. transmission doesn't actually support categories, so you must
          choose a directory as a category. eg /default/download/dir/music, where
          'music' is the category. this setup is made easy with a browser extension
          that supports custom download directories. eg. 'transmission easy client`
          for chrome.
</template>

<script>
// imports
import Service from '@/components/settings/Service.vue'
// import backend from '@/backend'
import { mapMutations, mapGetters, mapActions } from 'vuex'
// export
export default {
  components: {
    Service
  },
  computed: {
    ...mapGetters([
      'notificationSettingsGeneral',
      'notificationSettingsServices',
      'notificationSettingsPossibleServices'
    ])
  },
  methods: {
    ...mapMutations([
      'updateService'
    ]),
    ...mapActions([
      'removeNotificationSettingsService',
      'saveNotificationSettingsService',
      'addNotificationSettingsService'
    ]),
    testService () {
      // const fetchUrl = `settings/remotes/${this.remoteID}/test`
      // backend.fetchResource(fetchUrl)
      //   .then(response => {
      //     const type = response.ok ? 'is-green' : 'is-primary'
      //     const prefix = response.ok ? 'succeeded' : 'failed'
      //     this.$toast.open({
      //       message: `testing ${prefix}: ${response.reason}`,
      //       type
      //     })
      //   })
    }
  },
  data () {
    return {
      newServiceType: 'Kodi/XBMC'
    }
  }
}
</script>

<style scoped>
  td[data-label='enabled'] {
    width: 190px !important;
  }
  .switch-field {
    padding-top: 6px;
  }
  #buttons {
    padding-top: 12px;
  }
</style>
