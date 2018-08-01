import Vue from 'vue'
import Vuex from 'vuex'
import backend from './backend'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    downloads: [],
    haveDownloads: false
  },
  getters: {
    downloads: state => state.downloads,
    haveDownloads: state => state.haveDownloads
  },
  mutations: {
    setDownloads (state, downloads) {
      state.downloads = downloads
    },
    setHaveDownloads (state, have) {
      state.haveDownloads = have
    }
  },
  actions: {
    getDownloads ({ commit }) {
      backend.fetchResource('transmission')
        .then(result => {
          commit('setDownloads', result)
          commit('setHaveDownloads', true)
        })
        .catch(() => {
          commit('setHaveDownloads', true)
        })
    }
  }
})
