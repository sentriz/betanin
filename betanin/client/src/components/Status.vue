<template lang="pug">
  #status
    #left
      p(v-show='betaninVersion')
        | ver.&nbsp;
        b {{ betaninVersion | truncate(8, ' ') }}
    #right
      p(v-show='Object.keys(getStatus).length === 0') no status available
      p(v-for='count, key in getStatus')
        b {{ countString(count) }}
        span#explaination  {{ explaination(key, count) }}
</template>

<script>
// import
import { mapGetters } from 'vuex'
// help
const statusMap = {
  /* eslint-disable key-spacing */
  ENQUEUED:    ['is in the queue', 'are in the queue'],
  PROCESSING:  ['is being processed', 'are being processed'],
  NEEDS_INPUT: ['needs input', 'need input'],
  FAILED:      ['has failed', 'have failed'],
  WAITING:     ['is waiting to finish', 'are waiting to finish'],
  COMPLETED:   ['is completed', 'are completed'],
  DOWNLOADING: ['is downloading', 'are downloading']
}
// eslint-disable-next-line
const betaninVersion = __SOURCE_COMMIT__
// export
export default {
  computed: {
    ...mapGetters('status', [
      'getStatus'
    ])
  },
  data () {
    return {
      betaninVersion
    }
  },
  methods: {
    countString (count) {
      const suffix = count === 1 ? '' : 's'
      return `${count} torrent${suffix}`
    },
    explaination (key, count) {
      const preExp = statusMap[key]
      return preExp instanceof Array
        ? preExp[Number(count !== 1)]
        : preExp
    }
  }
}
</script>

<style lang="scss" scoped>
  p {
    text-align: right;
  }
  #explaination {
    font-weight: normal;
  }
  #status {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    @media only screen and (max-width: 1087px) {
      font-size: 0.8rem;
    }
  }
</style>
