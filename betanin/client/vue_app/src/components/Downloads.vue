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
          :appearance='statusToIconAppearance(props.row.status)'
        )
    template(slot-scope='props', slot='detail')
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
const statusMap = {
  /* eslint-disable no-multi-spaces, key-spacing */
  //                                      text shown     fa47 icon             colour of text and icon
  'RemoteStatus.COMPLETED':   appearToMap('downloaded',  'check',              'hsl(178, 92%,  29%)'), // green
  'RemoteStatus.DOWNLOADING': appearToMap('downloading', 'clock-o',            'hsl(228, 99%,  66%)'), // blue
  'RemoteStatus.INACTIVE':    appearToMap('paused',      'times',              'hsl(0,   0%,   86%)'), // light grey
  'BetaStatus.ENQUEUED':      appearToMap('equeued',     'clock-o',            'hsl(36,  99%,  65%)'), // orange
  'BetaStatus.PROCESSING':    appearToMap('processing',  'clock-o',            'hsl(48,  98%,  52%'),  // yellow
  'BetaStatus.NEEDS_INPUT':   appearToMap('needs input', 'exclamation-circle', 'hsl(48,  98%,  52%)'), // yellow-orange
  'BetaStatus.FAILED':        appearToMap('failed',      'times',              'hsl(349, 58%,  57%)'), // angry red
  'BetaStatus.COMPLETED':     appearToMap('completed',   'check',              'hsl(141, 71%,  48%)')  // green
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
    statusToIconAppearance (status) {
      return statusMap[status]
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
