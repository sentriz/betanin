import Vue from 'vue'

/* eslint-disable no-multi-spaces, key-spacing, complexity */
const binaryInsert = (array, item, startVal, endVal) => {
  const value  = Number(item.index)
  const length = array.length
  const start  = typeof startVal !== 'undefined' ? startVal : 0
  const end    = typeof endVal   !== 'undefined' ? endVal   : length - 1
  const middle = start + Math.floor((end - start) / 2)
  if      (length === 0)                array.push(item)
  else if (value > array[end].index)    array.splice(end + 1, 0, item)
  else if (value < array[start].index)  array.splice(start, 0, item)
  else if (value < array[middle].index) binaryInsert(array, item, start, middle - 1)
  else if (value > array[middle].index) binaryInsert(array, item, middle + 1, end)
}

export default {
  setDownloads (state, downloads) {
    state.downloads = downloads
  },
  appendLine (state, {torrentID, line}) {
    const lines = torrentID in state.lines
      ? state.lines[torrentID].concat()
      : []
    binaryInsert(lines, line)
    Vue.set(state.lines, torrentID, lines)
  },
  setConnected (state, connected) {
    state.connected = connected
  },
  updateRemoteConfig (state, {remoteID, key, value}) {
    const remoteIndex = state.remotes.findIndex(remote =>
      remote.id === remoteID
    )
    state.remotes[remoteIndex].config[key] = value
  },
  addRemote (state, data) {
    state.remotes.push(data)
  },
  clearRemotes (state) {
    state.remotes = []
  },
  removeRemote (state, remoteID) {
    state.remotes.splice(
      state.remotes.findIndex(remote =>
        remote.id === remoteID
      ),
      1
    )
  }
}
