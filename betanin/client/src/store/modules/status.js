import Vue from 'vue'
import { STATUS_CONNECTED_UPDATE } from '../mutation-types'

const state = {
  connected: false,
  status: {}
}

const getters = {
  getConnected: state =>
    state.connected
}

const actions = {
  doSocket__connect: ({ commit, dispatch }) => {
    commit(STATUS_CONNECTED_UPDATE, true)
  },
  doSocket__disconnect: ({ commit }) => {
    commit(STATUS_CONNECTED_UPDATE, false)
  }
}

const mutations = {
  [STATUS_CONNECTED_UPDATE] (state, connected) {
    Vue.set(state, 'connected', connected)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
