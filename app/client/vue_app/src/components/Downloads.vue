<template lang="pug">
  b-table(
    :data='downloads'
    :opened-detailed='openedDetails'
    detailed
    detail-key='id'
    :has-detailed-visible='rowHasDetail'
    v-if='haveDownloads'
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
        |  {{ props.row.percentDone }}%
  h3.title.is-5(
    v-else
  ) no downloads yet
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
      return row.isFinished === true
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
    background: #d1536a;
    color: #d1536a;
  }
  progress::-webkit-progress-value {
    background: #d1536a;
  }
  progress::-moz-progress-bar {
    background: #d1536a;
  }
  progress::-webkit-progress-value {
    background: #d1536a;
  }
  progress::-webkit-progress-bar {
    background: #d1536a;
  }
</style>
