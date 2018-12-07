import Vue from 'vue'
import backend from '@/backend'
import { itemFromID } from '../utilities'
import { TORRENTS_UPDATE } from '../mutation-types'

const state = {
  torrents: []
}

const getters = {
  getActivity: state =>
    state.torrents.filter(item =>
      item.status !== 'COMPLETED'),
  getHistory: state =>
    state.torrents.filter(item =>
      item.status === 'COMPLETED'),
  getActivityCount: (state, getters) =>
    getters.getActivity.length,
  getHistoryCount: (state, getters) =>
    getters.getHistory.length,
  getOne: state => torrentID =>
    itemFromID(state.torrents, torrentID)
}

const actions = {
  async doFetchAll ({ commit }) {
    const result = await backend.fetchResource('torrents/')
    commit(TORRENTS_UPDATE, result)
  },
  doDeleteOne (context, torrentID) {
    backend.deleteResource(`torrents/${torrentID}`)
  },
  doRetryOne (context, torrentID) {
    backend.putResource(`torrents/${torrentID}`)
  },
  doSocket__connect: ({ dispatch }) => {
    dispatch('doFetchAll')
  },
  doSocket__changed: ({ dispatch }) => {
    dispatch('doFetchAll')
  }
}

const mutations = {
  [TORRENTS_UPDATE] (state, torrents) {
    Vue.set(state, 'torrents', torrents)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
