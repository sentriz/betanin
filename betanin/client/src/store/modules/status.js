import Vue from 'vue'
import { STATUS_UPDATE, CONNECTED_UPDATE } from '../mutation-types'

const state = {
  connected: false,
  status: {}
}

const getters = {
  getStatus: state =>
    state.status,
  getConnected: state =>
    state.connected
}

const actions = {
  socket_connect: ({ commit, dispatch }) => {
    commit(CONNECTED_UPDATE, true)
  },
  socket_disconnect: ({ commit }) => {
    commit(CONNECTED_UPDATE, false)
  }
}

const mutations = {
  [STATUS_UPDATE] (state, status) {
    Vue.set(state, 'status', status)
  },
  [CONNECTED_UPDATE] (state, connected) {
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
