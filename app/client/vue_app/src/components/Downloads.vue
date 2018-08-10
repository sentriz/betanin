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
      b-table-column(label='finished')
        CheckMark(
          v-if='props.row.isFinished === true'
        )
        XMark(
          v-else
        )
    template(slot-scope='props', slot='detail')
      p
        strong downloaded
        |  {{ props.row.progress }}%
</template>

<script>
import CheckMark from '@/components/icons/CheckMark.vue'
import XMark from '@/components/icons/XMark.vue'
import { mapGetters } from 'vuex'
export default {
  computed: mapGetters([
    'downloads',
    'haveDownloads'
  ]),
  components: {
    CheckMark,
    XMark
  },
  methods: {
    rowHasDetail (row) {
      return true
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
