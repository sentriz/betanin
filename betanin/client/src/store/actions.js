import backend from '@/backend'

export default {
  getDownloads ({ commit }) {
    backend.fetchResource('torrents/')
      .then(result => {
        commit('setDownloads', result.torrents)
        commit('setStatus', result.status)
      })
  },
  // last lines from ajax
  getLines ({ commit }, torrentID) {
    const fetchUrl = `torrents/${torrentID}/console/stdout`
    backend.fetchResource(fetchUrl)
      .then(lines => {
        lines.forEach(line => {
          commit('appendLine', { torrentID, line })
        })
      })
  },
  socket_changed: ({ dispatch }) => {
    dispatch('getDownloads')
  },
  // one line from socket
  socket_read: ({ commit }, { torrentID, line }) => {
    commit('appendLine', { torrentID, line })
  },
  socket_connect: ({ commit, dispatch }) => {
    commit('setConnected', true)
    dispatch('getDownloads')
  },
  socket_disconnect: ({ commit }) => {
    commit('setConnected', false)
  }
}
