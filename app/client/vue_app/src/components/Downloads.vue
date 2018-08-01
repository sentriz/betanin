<template lang="pug">
  b-table(
    :data='downloads'
    :loading='!haveDownloads'
    :opened-detailed='openedDetails'
    detailed
    detail-key='id'
    :has-detailed-visible='rowHasDetail'
  )
    template(slot-scope='props')
      b-table-column(label='name') {{ props.row.name }}
      b-table-column(
        label='progress'
        width='200'
      )
        progress.progress(
          :value='props.row.percentDone'
          max='100'
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
</style>
