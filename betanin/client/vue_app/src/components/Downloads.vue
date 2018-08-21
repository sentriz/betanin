<template lang="pug">
  b-table(
    :data='downloads'
    :opened-detailed='openedDetails'
    detailed
    detail-key='id'
    :has-detailed-visible='rowHasDetail'
    :loading='!haveDownloads'
    @details-open='onDetails'
  )
    template(
      slot-scope='props'
    )
      b-table-column(
        label='name'
      ) {{ props.row.name }}
      b-table-column(
        label='progress'
      )
        progress(
          :value='props.row.progress'
          max="100"
        )
        | &nbsp; {{ props.row.progress | round }}%
      b-table-column(label='status')
        BTooltip(
          :active='props.row.tooltip !== null'
          :label='props.row.tooltip'
          multiline
          dashed
        )
          Icon(
            :appearance='betAppear(props.row.beta_status)'
          )
    template(slot-scope='props', slot='detail')
      p
        strong remote status
        |  {{ props.row.remote_status | lower }}
      p
        strong betanin status
        |  {{ props.row.beta_status | lower }}
      p
        strong downloaded
        |  {{ props.row.progress }}%
      p(
        v-for='line in lines(props.row.id)'
      ) {{ line.index }} - {{ line.data }}
</template>

<script>
// imports
import Console from '@/components/Console.vue'
import Icon from '@/components/Icon.vue'
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
      'downloads',
      'lines',
      'haveDownloads'
    ])
  },
  components: {
    Icon,
    Console
  },
  methods: {
    ...mapActions([
      'getLines'
    ]),
    rowHasDetail (row) {
      return true
    },
    betAppear (status) {
      return betaStatusMap[status]
    },
    onDetails (row) {
      if (this.doneAJAX.includes(row.id)) {
        return
      }
      this.getLines(row.id)
      this.doneAJAX.push(row.id)
    }
  },
  filters: {
    round (value) {
      return Math.round(value)
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
