import Vue from 'vue'

/* eslint-disable no-multi-spaces, key-spacing */
const binaryInsert = (item, array, startVal, endVal) => {
  const value  = Number(item.index)
  const length = array.length
  const start  = typeof startVal !== "undefined" ? startVal : 0
  const end    = typeof endVal   !== "undefined" ? endVal   : length - 1
  const middle = start + Math.floor((end - start) / 2)
  if      (length === 0)                array.push(item)
  else if (value > array[end].index)    array.splice(end + 1, 0, item)
  else if (value < array[start].index)  array.splice(start, 0, item)
  else if (value < array[middle].index) binaryInsert(item, array, start, middle - 1)
  else if (value > array[middle].index) binaryInsert(item, array, middle + 1, end)
}

export default {
  setDownloads (state, downloads) {
    state.downloads = downloads
  },
  appendLine (state, {torrentID, line}) {
    const lines = torrentID in state.lines
      ? state.lines[torrentID].concat()
      : []
    binaryInsert(line, lines)
    Vue.set(state.lines, torrentID, lines)
  },
  setConnected (state, connected) {
    state.connected = connected
  }
}
