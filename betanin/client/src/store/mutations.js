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
  setTorrents (state, torrents) {
    Vue.set(state, 'torrents', torrents)
  },
  setStatus (state, status) {
    Vue.set(state, 'status', status)
  },
  setNotificationSettings (state, settings) {
    Vue.set(state, 'notificationSettingsServices', settings)
  },
  setNotificationSettingsPossibleServices (state, possibleServices) {
    Vue.set(state, 'notificationSettingsPossibleServices', possibleServices)
  },
  removeNotificationSettingsService (state, serviceID) {
    state.notificationSettingsServices.splice(
      state.notificationSettingsServices.findIndex(service =>
        service.id === serviceID
      ),
      1
    )
  },
  updateService (state, { serviceID, key, value }) {
    const serviceIndex = state.notificationSettingsServices.findIndex(service =>
      service.id === serviceID
    )
    Vue.set(state.notificationSettingsServices[serviceIndex], key, value)
  },
  addNotificationSettingsService (state, service) {
    state.notificationSettingsServices.push(service)
  },
  appendLine (state, { torrentID, line }) {
    const lines = torrentID in state.lines
      ? state.lines[torrentID].concat()
      : []
    binaryInsert(lines, line)
    Vue.set(state.lines, torrentID, lines)
  },
  markLinesFetched (state, torrentID) {
    const linesCopy = state.fetchedLines.concat()
    linesCopy.push(torrentID)
    Vue.set(state, 'fetchedLines', linesCopy)
  },
  setConnected (state, connected) {
    Vue.set(state, 'connected', connected)
  }
}
