import Vue from 'vue'
import backend from '@/backend'
import {
  binaryInsert,
  cleanObject
} from '../utilities'
import { LINES_CREATE } from '../mutation-types'

const state = {
  lines: {}
}

const getters = {
  getByID: state =>
    state.lines
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
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true
}
