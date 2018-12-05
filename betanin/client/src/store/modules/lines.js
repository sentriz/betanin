import Vue from 'vue'
import backend from '@/backend'
import { binaryInsert, lastN } from '../utilities'
import { LINES_CREATE, LINES_FETCHED_CREATE } from '../mutation-types'

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
    const lines = await backend.fetchResource(`torrents/${torrentID}/console/stdout`)
    lines.forEach(line => {
      commit(LINES_CREATE, { torrentID, line })
    })
  },
  doSocket__read ({ commit }, { torrentID, line }) {
    commit(LINES_CREATE, { torrentID, line })
  }
}

const mutations = {
  [LINES_CREATE] (state, { torrentID, line }) {
    const lines = torrentID in state.lines
      ? state.lines[torrentID].concat()
      : []
    binaryInsert(lines, line)
    Vue.set(state.lines, torrentID, lines)
  },
  [LINES_FETCHED_CREATE] (state, torrentID) {
    const copy = state.fetched.concat()
    copy.push(torrentID)
    Vue.set(state, 'fetched', copy)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
