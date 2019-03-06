import Vue from 'vue'
import backend from '@/backend'
import {
  binaryInsert,
  lastN,
  cleanObject
} from '../utilities'
import {
  LINES_CREATE,
  LINES_FETCHED_CREATE
} from '../mutation-types'

const state = {
  lines: {},
  fetched: []
}

const getters = {
  getAll: state => (torrentID, lineLimit) =>
    lastN(state.lines[torrentID] || [], lineLimit),
  getExists: state => torrentID =>
    Boolean(state.lines[torrentID]),
  getFetched: state => torrentID =>
    state.fetched.includes(torrentID)
}

const actions = {
  async doFetchAll ({ commit }, torrentID) {
    const lines = await backend.secureAxios.get(
      `torrents/${torrentID}/console/stdout`)
    lines.data.forEach(line => {
      commit(LINES_CREATE, { torrentID, ...line })
    })
  },
  doSocket__newLine ({ commit }, data) {
    const cleanData = cleanObject(data)
    commit(LINES_CREATE, cleanData)
  }
}

const mutations = {
  [LINES_CREATE] (state, { torrentID, index, data }) {
    const lines = torrentID in state.lines
      ? state.lines[torrentID]
      : []
    binaryInsert(lines, { index, data })
    Vue.set(state.lines, torrentID, lines)
  },
  [LINES_FETCHED_CREATE] (state, torrentID) {
    state.fetched.push(torrentID)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
