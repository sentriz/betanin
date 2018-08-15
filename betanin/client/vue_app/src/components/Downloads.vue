<template lang="pug">
  b-table(
    :data='downloads'
    :opened-detailed='openedDetails'
    detailed
    detail-key='id'
    :has-detailed-visible='rowHasDetail'
    :loading='!haveDownloads'
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
</template>

<script>
import Icon from '@/components/Icon.vue'
import { mapGetters } from 'vuex'
const appearToMap = (text, icon, colour) => ({
  text, icon, colour
})
// const remoteStatusMap = {
//   /* eslint-disable no-multi-spaces, key-spacing */
//   //                         text shown     fa47 icon  colour of text and icon
//   'COMPLETED':   appearToMap('downloaded',  'check',   'hsl(178, 92%, 29%)'), // green
//   'DOWNLOADING': appearToMap('downloading', 'clock-o', 'hsl(228, 99%, 66%)'), // blue
//   'INACTIVE':    appearToMap('paused',      'times',   'hsl(0,   0%,  86%)')  // light grey
// }
const betaStatusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  //                         text shown     fa47 icon             colour of text and icon
  'ENQUEUED':    appearToMap('equeued',     'clock-o',            'hsl(36,  99%,  65%)'), // orange
  'PROCESSING':  appearToMap('processing',  'clock-o',            'hsl(48,  98%,  52%'),  // yellow
  'NEEDS_INPUT': appearToMap('needs input', 'exclamation-circle', 'hsl(48,  98%,  52%)'), // yellow-orange
  'FAILED':      appearToMap('failed',      'times',              'hsl(349, 58%,  57%)'), // angry red
  'COMPLETED':   appearToMap('completed',   'check',              'hsl(141, 71%,  48%)'), // green
  'UNKNOWN':     appearToMap('unknown',     'exclamation-circle', 'hsl(0,   0%,  86%)')   // light grey
}
export default {
  computed: mapGetters([
    'downloads',
    'haveDownloads'
  ]),
  components: {
    Icon
  },
  methods: {
    rowHasDetail (row) {
      return true
    },
    betAppear (status) {
      return betaStatusMap[status]
    }
  },
  filters: {
    round (value) {
      return Math.round(value)
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
</style>
