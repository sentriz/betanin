import Vue from 'vue'
import backend from '@/backend'
import { itemFromID } from '../utilities'
import { TORRENTS_UPDATE, STATUS_UPDATE } from '../mutation-types'

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
  getOne: state => torrentID =>
    itemFromID(state.torrents, torrentID)
}

const actions = {
  doFetchAll ({ commit }) {
    backend.fetchResource('torrents/')
      .then(result => {
        commit(TORRENTS_UPDATE, result.torrents)
        commit(`status/${STATUS_UPDATE}`, result.status, { root: true })
      })
  },
  doDeleteOne (torrentID) {
    backend.deleteResource(`torrents/${torrentID}`)
  },
  doRetryOne (torrentID) {
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
