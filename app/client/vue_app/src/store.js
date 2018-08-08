import Vue from 'vue'
import Vuex from 'vuex'
import backend from './backend'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    downloads: []
  },
  getters: {
    downloads: state =>
      state.downloads,
    haveDownloads: state =>
      state.downloads.length !== 0
  },
  mutations: {
    setDownloads (state, downloads) {
      state.downloads = downloads
    }
  },
  actions: {
    getDownloads ({ commit }) {
      backend.fetchResource('torrents/all')
        .then(result => {
          commit('setDownloads', result)
        })
    }
  }
})
