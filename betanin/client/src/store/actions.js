import backend from '@/backend'

export default {
  getDownloads ({commit}) {
    backend.fetchResource('torrents/')
      .then(result => {
        commit('setDownloads', result)
      })
  },
  getSettings ({commit}) {
    backend.fetchResource('settings/remotes/')
      .then(remotes => {
        remotes.forEach(remote => {
          commit('addRemote', remote)
        })
      })
  },
  // last lines from ajax
  getLines ({commit}, torrentID) {
    const fetchUrl = `torrents/${torrentID}/console/stdout`
    backend.fetchResource(fetchUrl)
      .then(lines => {
        lines.forEach(line => {
          commit('appendLine', {torrentID, line})
        })
      })
  },
  removeRemote ({commit}, {remoteID}) {
    // delete from api
    commit('removeRemote', remoteID)
  },
  addRemote ({commit}, type) {
    const fetchUrl = `settings/remotes?type=${type}`
    console.log(fetchUrl)
    backend.postResource(fetchUrl)
      .then(data => {
        console.log('new remote', data)
        commit('addRemote', data)
      })
  },
  socket_grabbed: ({dispatch}) => {
    dispatch('getDownloads')
  },
  // one line from socket
  socket_read: ({commit}, {torrentID, line}) => {
    commit('appendLine', {torrentID, line})
  },
  socket_connect: ({commit, dispatch}) => {
    commit('setConnected', true)
    dispatch('getSettings')
    dispatch('getDownloads')
  },
  socket_disconnect: ({commit}) => {
    commit('setConnected', false)
  }
}
