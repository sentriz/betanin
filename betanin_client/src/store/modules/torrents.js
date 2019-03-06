import Vue from 'vue'
import backend from '@/backend'
import { itemFromID } from '../utilities'
import {
  TORRENTS_ALL_CREATE,
  TORRENTS_ONE_UPDATE,
  TORRENTS_ONE_DELETE
} from '../mutation-types'

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
    const result = await backend.secureAxios.get('torrents/')
    commit(TORRENTS_ALL_CREATE, result.data)
  },
  doDeleteOne ({ commit }, torrentID) {
    backend.secureAxios.delete(`torrents/${torrentID}`)
    commit(TORRENTS_ONE_DELETE, torrentID)
  },
  doRetryOne (context, torrentID) {
    backend.secureAxios.put(`torrents/${torrentID}`)
  },
  doSocket__newTorrent: ({ commit }, torrent) => {
    commit(TORRENTS_ONE_UPDATE, torrent)
  }
}

const mutations = {
  [TORRENTS_ALL_CREATE] (state, torrents) {
    Vue.set(state, 'torrents', torrents)
  },
  [TORRENTS_ONE_UPDATE] (state, torrent) {
    const i = state.torrents.findIndex(item =>
      item.id === torrent.id)
    if (i > -1) {
      Vue.set(state.torrents, i, torrent)
      return
    }
    state.torrents.unshift(torrent)
  },
  [TORRENTS_ONE_DELETE] (state, torrentID) {
    state.torrents.splice(
      state.torrents.findIndex(torrent =>
        torrent.id === torrentID), 1
    )
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
