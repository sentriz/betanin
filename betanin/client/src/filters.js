import Vue from 'vue'

const filters = {
  formatTimestamp (timestamp) {
    const datetime = new Date(timestamp)
    return datetime.toLocaleTimeString('en-IE')
  },
  lower (string) {
    return string.toLowerCase()
  },
  round (value) {
    return Math.round(value)
  }
}

Object.keys(filters).forEach(filterName => {
  Vue.filter(filterName, filters[filterName])
})
