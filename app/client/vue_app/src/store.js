import Vue from 'vue'
import Vuex from 'vuex'
import backend from './backend'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    downloads: [],
    connected: false
  },
  getters: {
    downloads: state =>
      state.downloads,
    haveDownloads: state =>
      state.downloads.length !== 0,
    connected: state =>
      state.connected
  },
  mutations: {
    setDownloads (state, downloads) {
      state.downloads = downloads
    },
    setConnected (state, connected) {
      state.connected = connected
    }
  },
  actions: {
    getDownloads ({ commit }) {
      backend.fetchResource('torrents/all')
        .then(result => {
          commit('setDownloads', result)
        })
      console.log('fetched downloads')
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
