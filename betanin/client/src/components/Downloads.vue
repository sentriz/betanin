<template lang="pug">
  div
    b-table(:data='downloads'
            :opened-detailed='openedDetails'
            detailed
            detail-key='id'
            :has-detailed-visible='rowHasDetail'
            @details-open='onDetails')
      template(slot-scope='props')
        b-table-column(label='client') {{ remoteTag(props.row.remote_id) }}
        b-table-column(label='name') {{ props.row.name }}
        b-table-column(label='progress')
          progress(:value='props.row.progress' max="100")
            | &nbsp; {{ props.row.progress | round }}%
        b-table-column(label='status' :numeric='true')
          span#console-link(
            v-show='areLines(props.row.id)'
            @click='openModal(props.row.id)'
          )
            b-icon(icon='console' size='is-small')
            |  view &nbsp;
          b-tooltip(:active='props.row.tooltip !== null'
                    :label='props.row.tooltip'
                    multiline
                    dashed)
            icon(:appearance='betAppear(props.row.beta_status)')
      template(slot-scope='props'
               slot='detail')
        .level
          .level-left
            preview-console(v-show='areLines(props.row.id)'
                            :torrentID='props.row.id')
          .level-right
            #row-status
              p
                strong remote status
                |  {{ props.row.remote_status | lower }}
              p
                strong betanin status
                |  {{ props.row.beta_status | lower }}
              p
                strong downloaded
                |  {{ props.row.progress }}%
      template(slot='empty')
        h6(v-show='!haveDownloads')
          b-icon(icon='alert')
          | &nbsp; no downloads to process yet, check the status below
      template(slot='footer')
        status
</template>

<script>
// imports
import ModalConsole from '@/components/console/ModalConsole.vue'
import Icon from '@/components/Icon.vue'
import Status from '@/components/Status.vue'
import { mapGetters, mapActions } from 'vuex'
// help
const appearToMap = (text, icon, colour) => ({
  text, icon, colour
})
const betaStatusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  //                         text shown     mdi28 icon       colour
  'ENQUEUED':    appearToMap('equeued',     'clock-outline', 'hsl(36,  99%,  65%)'), // orange
  'PROCESSING':  appearToMap('processing',  'clock-fast',    'hsl(48,  98%,  52%'),  // yellow
  'NEEDS_INPUT': appearToMap('needs input', 'alert',         'hsl(48,  98%,  52%)'), // yellow-orange
  'FAILED':      appearToMap('failed',      'close',         'hsl(349, 58%,  57%)'), // angry red
  'COMPLETED':   appearToMap('completed',   'check',         'hsl(141, 71%,  48%)'), // green
  'WAITING':     appearToMap('waiting',     'sleep',         'hsl(0,   0%,  86%)'),  // light grey
  'UNKNOWN':     appearToMap('unknown',     'file-unknown',  'hsl(0,   0%,  86%)')   // light grey
}
// export
export default {
  computed: {
    ...mapGetters([
      'activeModal',
      'areLines',
      'downloads',
      'haveDownloads',
      'lines',
      'remoteTypeFromID'
    ])
  },
  components: {
    Icon,
    Status
  },
  methods: {
    ...mapActions([
      'getLines'
    ]),
    rowHasDetail (torrent) {
      return torrent.beta_status !== 'IGNORED'
    },
    onDetails (torrent) {
      if (this.doneAJAX.includes(torrent.id)) {
        return
      }
      this.getLines(torrent.id)
      this.doneAJAX.push(torrent.id)
    },
    betAppear (status) {
      return betaStatusMap[status]
    },
    remoteTag (remoteID) {
      const type = this.remoteTypeFromID(remoteID)
      const uid = remoteID === 1
        ? ''
        : ` #${remoteID}`
      return `${type}${uid}`
    },
    openModal (torrentID) {
      this.$modal.open({
        parent: this,
        component: ModalConsole,
        props: { torrentID },
        hasModalCard: true
      })
    }
  },
  data () {
    return {
      openedDetails: [],
      doneAJAX: []
    }
  }
}
</script>

<style scoped>
  progress {
    display: inline-block;
    border: none;
    -webkit-appearance: none;
  }
  /* background */
  progress::-webkit-progress-bar {
    background: #eeeeee;
  }
  /* foreground */
  progress::-webkit-progress-value {
    background: #d1536a;
  }
  .level {
    padding-bottom: 0;
  }
  #row-status {
    text-align: right;
  }
</style>
