import backend from '@/backend'

export default {
  getNotificationSettings ({ commit }) {
    backend.fetchResource('settings/notifications/services')
      .then(result => {
        commit('setNotificationSettings', result)
      })
  },
  getNotificationSettingsPossibleServices ({ commit }) {
    backend.fetchResource('settings/notifications/possible_services')
      .then(result => {
        commit('setNotificationSettingsPossibleServices', result.schemas)
      })
  },
  removeNotificationSettingsService ({ commit }, serviceID) {
    backend.deleteResource(`settings/notifications/services/${serviceID}`)
      .then(result => {
        commit('removeNotificationSettingsService', serviceID)
      })
  },
  saveNotificationSettingsService ({ commit, getters }, serviceID) {
    const service = getters.serviceFromID(serviceID)
    backend.putResource(
      `settings/notifications/services/${serviceID}`,
      service
    )
  },
  addNotificationSettingsService ({ commit }, serviceType) {
    backend.postResource(
      `settings/notifications/services`,
      { type: serviceType }
    ).then(result => {
      commit('addNotificationSettingsService', result)
    })
  },
  getTorrents ({ commit }) {
    backend.fetchResource('torrents/')
      .then(result => {
        commit('setTorrents', result.torrents)
        commit('setStatus', result.status)
      })
  },
  removeTorrent ({ commit }, torrentID) {
    backend.deleteResource(`torrents/${torrentID}`)
  },
  retryTorrent ({ commit }, torrentID) {
    backend.putResource(`torrents/${torrentID}`)
  },
  // last lines from ajax
  getLines ({ commit }, torrentID) {
    backend.fetchResource(`torrents/${torrentID}/console/stdout`)
      .then(lines => {
        lines.forEach(line => {
          commit('appendLine', { torrentID, line })
        })
      })
  },
  socket_changed: ({ dispatch }) => {
    dispatch('getTorrents')
  },
  // one line from socket
  socket_read: ({ commit }, { torrentID, line }) => {
    commit('appendLine', { torrentID, line })
  },
  socket_connect: ({ commit, dispatch }) => {
    commit('setConnected', true)
    dispatch('getTorrents')
    dispatch('getNotificationSettings')
    dispatch('getNotificationSettingsPossibleServices')
  },
  socket_disconnect: ({ commit }) => {
    commit('setConnected', false)
  }
}
