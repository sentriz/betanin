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
        b-table-column(label='status')
          b-tooltip(:active='props.row.tooltip !== null'
                    :label='props.row.tooltip'
                    multiline
                    dashed)
            Icon(:appearance='betAppear(props.row.beta_status)')
      template(slot-scope='props'
               slot='detail')
        .columns
          .column
            preview-console(v-show='areLines(props.row.id)'
                            :torrentID='props.row.id')
          .column
            .is-pulled-right
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
          b-icon(icon='exclamation-triangle')
          | &nbsp; no downloads to process yet, check the status below
      template(slot='footer')
        status.is-pulled-right
</template>

<script>
// imports
import Icon from '@/components/Icon.vue'
import PreviewConsole from '@/components/console/PreviewConsole.vue'
import Status from '@/components/Status.vue'
import { mapGetters, mapActions } from 'vuex'
// help
const appearToMap = (text, icon, colour) => ({
  text, icon, colour
})
const betaStatusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  //                         text shown     fa47 icon             colour of text and icon
  'ENQUEUED':    appearToMap('equeued',     'clock-o',            'hsl(36,  99%,  65%)'), // orange
  'PROCESSING':  appearToMap('processing',  'clock-o',            'hsl(48,  98%,  52%'),  // yellow
  'NEEDS_INPUT': appearToMap('needs input', 'exclamation-circle', 'hsl(48,  98%,  52%)'), // yellow-orange
  'FAILED':      appearToMap('failed',      'times',              'hsl(349, 58%,  57%)'), // angry red
  'COMPLETED':   appearToMap('completed',   'check',              'hsl(141, 71%,  48%)'), // green
  'WAITING':     appearToMap('waiting',     'bed',                'hsl(0,   0%,  86%)'),  // light grey
  'UNKNOWN':     appearToMap('unknown',     'exclamation-circle', 'hsl(0,   0%,  86%)'),  // light grey
  'IGNORED':     appearToMap('ignored',     'times',              'hsl(36,  99%,  65%)')  // orange
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
    PreviewConsole,
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
</style>
