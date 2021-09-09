<template lang="pug">
span(:style='{ color: style.colour }')
  b-icon(:icon='style.icon', size='is-small')
  |
  | {{ style.text }}
</template>

<script>
const statusMap = {
  ENQUEUED: {
    text: 'enqueued',
    icon: 'clock-outline',
    colour: 'hsl(36, 99%, 65%)',
  },
  PROCESSING: {
    text: 'processing',
    icon: 'clock-fast',
    colour: 'hsl(48, 98%, 52%',
  },
  NEEDS_INPUT: {
    text: 'needs input',
    icon: 'alert',
    colour: 'hsl(48, 98%, 52%)',
  },
  FAILED: { text: 'failed', icon: 'close', colour: 'hsl(349, 58%, 57%)' },
  COMPLETED: { text: 'completed', icon: 'check', colour: 'hsl(141, 71%, 48%)' },
}
// export
export default {
  props: ['status'],
  computed: {
    style() {
      return statusMap[this.status]
    },
  },
}
</script>
