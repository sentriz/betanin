import backend from '@/backend'

export default {
  getDownloads ({ commit }) {
    backend.fetchResource('torrents/')
      .then(result => {
        commit('setDownloads', result)
      })
    console.log('fetched downloads')
  },
  // last lines from ajax
  getLines ({ commit }, torrentID) {
    console.log('got ajax lines')
    const fetchUrl = 'torrents/' + torrentID + '/console'
    backend.fetchResource(fetchUrl)
      .then(lines => {
        lines.forEach(line => {
          commit('appendLine', {torrentID, line})
        })
      })
  },
  socket_grabbed: ({ dispatch }) => {
    dispatch('getDownloads')
  },
  // one line from socket
  socket_read: ({ commit }, {torrentID, line}) => {
    console.log('got socket line')
    commit('appendLine', {torrentID, line})
  },
  socket_connect: ({ commit, dispatch }) => {
    commit('setConnected', true)
    dispatch('getDownloads')
  },
  socket_disconnect: ({ commit }) => {
    commit('setConnected', false)
  }
}
