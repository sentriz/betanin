<template lang="pug">
  div
    b-table(:data='getServices')
      template(slot-scope='props')
        b-table-column(
          label='enabled'
        )
          b-field.switch-field
            b-switch(
              :value='props.row.enabled'
              @input=`genFieldSetter(props.row.id, 'enabled', $event)`
            ) {{ ['no', 'yes'][Number(props.row.enabled)] }}
        b-table-column(label='url')
          b-field
            p.control
              b-input(
                icon='earth'
                placeholder='eggs'
                :value='props.row.url'
                @input=`genFieldSetter(props.row.id, 'url', $event)`
              )
        b-table-column
          b-field(grouped group-multiline position='is-right')
            p.control
              button.button(@click='doPutService(props.row.id)').is-light save
            p.control
              button.button(@click='testService(props.row.id)').is-light test
            p.control
              button.button(@click='doDeleteService(props.row.id)').is-primary remove
      template(slot='footer')
        .field.has-addons.is-pulled-right
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
      template(slot='empty')
        h6(v-show='getServices.length === 0')
          b-icon(icon='alert')
          | &nbsp; no services here yet, add one below
    #empty-sep(v-show='getServices.length === 0')
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
import { NOTI_SERVICE_UPDATE } from '@/store/mutation-types'
import { mapMutations, mapGetters, mapActions } from 'vuex'
// help
// export
export default {
  components: {
    Service
  },
  computed: {
    ...mapGetters('notifications', [
      'getGeneral',
      'getServices',
      'getPossible'
    ])
  },
  methods: {
    genFieldSetter (serviceID, key, value) {
      this[NOTI_SERVICE_UPDATE]({ serviceID, key, value })
    },
    ...mapMutations('notifications', [
      NOTI_SERVICE_UPDATE
    ]),
    ...mapActions('notifications', [
      'doPostService',
      'doDeleteService',
      'doPutService'
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
      newServiceType: 'Kodi/XBMC',
      form: [
        { weed: 'greed' },
        { weed: 'greeds' },
        { weed: 'greedfsdf' }
      ]
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
