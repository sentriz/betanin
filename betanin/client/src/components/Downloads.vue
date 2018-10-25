<template lang="pug">
  div
    b-table(:data='downloads'
            :opened-detailed='openedDetails'
            detailed
            detail-key='id')
      template(slot-scope='props')
        b-table-column(label='client') {{ remoteTag(props.row.remote_id) }}
        b-table-column(label='name') {{ props.row.name | truncate(64) }}
        b-table-column(label='progress')
          progress(:value='props.row.progress' max="100")
            | &nbsp; {{ props.row.progress | round }}%
        b-table-column(label='status' :numeric='true')
          span#console-link(
            v-show='props.row.has_lines'
            @click='openModal(props.row.id)'
          )
            b-icon(icon='console' size='is-small')
            |  open &nbsp;
          b-tooltip(:active='props.row.tooltip !== null'
                    :label='props.row.tooltip'
                    multiline
                    dashed)
            icon(:appearance='betAppear(props.row.status)')
      template(slot-scope='props'
               slot='detail')
        .level
          .level-left
            preview-console(v-show='areLines(props.row.id)'
                            :torrentID='props.row.id')
          .level-right
            #row-status
              p
                strong id
                |  {{ props.row.id | truncate(10) }}
              p
                strong status
                |  {{ props.row.status | lower }}
              p
                strong downloaded
                |  {{ props.row.progress }}%
      template(slot='empty')
        h6(v-show='downloads.length === 0')
          b-icon(icon='alert')
          | &nbsp; no downloads here yet, check the status below
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
const statusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  //                         text shown     mdi28 icon       colour
  'ENQUEUED':    appearToMap('equeued',     'clock-outline', 'hsl(36,  99%,  65%)'), // orange
  'PROCESSING':  appearToMap('processing',  'clock-fast',    'hsl(48,  98%,  52%'),  // yellow
  'NEEDS_INPUT': appearToMap('needs input', 'alert',         'hsl(48,  98%,  52%)'), // yellow-orange
  'FAILED':      appearToMap('failed',      'close',         'hsl(349, 58%,  57%)'), // angry red
  'PROCESSED':   appearToMap('completed',   'check',         'hsl(141, 71%,  48%)'), // green
  'DOWNLOADING': appearToMap('downloading', 'sleep',         'hsl(0,   0%,  86%)')   // light grey
}
// export
export default {
  computed: {
    ...mapGetters([
      'activeModal',
      'areLines',
      'haveDownloads',
      'lines',
      'remoteTypeFromID'
    ])
  },
  components: {
    Icon,
    Status
  },
  props: [
    'downloads'
  ],
  methods: {
    ...mapActions([
      'getLines'
    ]),
    betAppear (status) {
      return statusMap[status]
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
      openedDetails: []
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
