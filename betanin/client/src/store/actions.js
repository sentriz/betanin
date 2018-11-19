import backend from '@/backend'

export default {
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
  },
  socket_disconnect: ({ commit }) => {
    commit('setConnected', false)
  }
}
