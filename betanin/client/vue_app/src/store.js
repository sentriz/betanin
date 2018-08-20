import Vue from 'vue'
import Vuex from 'vuex'
import backend from './backend'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    downloads: [],
    lines: {},
    connected: false
  },
  getters: {
    downloads: state =>
      state.downloads,
    lines: state => torrentID =>
      state.lines[torrentID],
    connected: state =>
      state.connected,
    haveDownloads: state =>
      state.downloads.length !== 0,
    areLines: state => torrentID =>
      state.lines[torrentID] && state.lines[torrentID].length !== 0
  },
  mutations: {
    setDownloads (state, downloads) {
      state.downloads = downloads
    },
    setLines (state, {torrentID, lines}) {
      Vue.set(state.lines, torrentID, lines)
      console.log('set', lines.length, 'lines')
    },
    setConnected (state, connected) {
      state.connected = connected
    }
  },
  actions: {
    getDownloads ({ commit }) {
      backend.fetchResource('torrents/')
        .then(result => {
          commit('setDownloads', result)
        })
      console.log('fetched downloads')
    },
    getLines ({ commit }, torrentID) {
      const fetchUrl = 'torrents/' + torrentID + '/console'
      backend.fetchResource(fetchUrl)
        .then(lines => {
          commit('setLines', {torrentID, lines})
        })
    },
    socket_grabbed: ({ dispatch }) => {
      dispatch('getDownloads')
    },
    socket_connect: ({ commit, dispatch }) => {
      commit('setConnected', true)
      dispatch('getDownloads')
    },
    socket_disconnect: ({ commit }) => {
      commit('setConnected', false)
    }
  }
})
