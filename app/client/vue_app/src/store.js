import Vue from 'vue'
import Vuex from 'vuex'
import backend from './backend'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    downloads: [],
    downloadsDone: false
  },
  getters: {
    downloads: state => state.downloads,
    downloadsDone: state => state.downloadsDone
  },
  mutations: {
    setDownloads (state, downloads) {
      state.downloads = downloads
      state.downloadsDone = true
    }
  },
  actions: {
    getDownloads ({ commit }) {
      backend.fetchResource('transmission').then(result =>
        commit('setDownloads', result)
      )
    }
  }
})
