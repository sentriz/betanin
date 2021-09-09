import Vue from 'vue'
import backend from '@/backend'
import { TORRENTS_ALL_APPEND, TORRENTS_ONE_UPDATE, TORRENTS_ONE_DELETE } from '@/store/mutation-types'

const state = {
  torrents: {},
  total: 0,
}

const getters = {
  getTorrent: (state) => (id) => state.torrents[id],
  getTotal: (state) => state.total,
  getActive: (state) => Object.values(state.torrents).filter((item) => item.status !== 'COMPLETED'),
  getActiveCount: (state, getters) => getters.getActive.length,
}

const actions = {
  doFetchOne({ commit }, torrentID) {
    const result = backend.secureAxios.get(`torrents/${torrentID}`)
    commit(TORRENTS_ONE_UPDATE, result.data)
  },
  doDeleteOne({ commit }, torrentID) {
    backend.secureAxios.delete(`torrents/${torrentID}`)
    commit(TORRENTS_ONE_DELETE, torrentID)
  },
  doRetryOne(context, torrentID) {
    backend.secureAxios.put(`torrents/${torrentID}`)
  },
  doSocket__newTorrent({ commit }, torrent) {
    commit(TORRENTS_ONE_UPDATE, torrent)
  },
}

const mutations = {
  [TORRENTS_ALL_APPEND](state, { total, torrents }) {
    Vue.set(state, 'total', total)
    for (const torrent of torrents) Vue.set(state.torrents, torrent.id, torrent)
  },
  [TORRENTS_ONE_UPDATE](state, torrent) {
    Vue.set(state.torrents, torrent.id, torrent)
  },
  [TORRENTS_ONE_DELETE](state, torrentID) {
    Vue.delete(state.torrents, torrentID)
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true,
}
