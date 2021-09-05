import Vue from 'vue'
import backend from '@/backend'
import keyBy from 'lodash.keyby'
import { ToastProgrammatic as Toast } from 'buefy'
import {
  NOTI_STRINGS_UPDATE,
  NOTI_STRING_UPDATE,
  NOTI_POSSIBLE_UPDATE,
  NOTI_SERVICES_UPDATE,
  NOTI_SERVICE_CREATE,
  NOTI_SERVICE_DELETE,
  NOTI_SERVICE_UPDATE,
  NOTI_SERVICE_TESTING_UPDATE,
} from '../mutation-types'

const state = {
  strings: {},
  services: [],
  possible: [],
  isTesting: false,
}

const getters = {
  getStrings: (state) => state.strings,
  getPossible: (state) => state.possible,
  getServices: (state) => state.services,
  getIsTesting: (state) => state.isTesting,
  getServiceByID: (state) => keyBy(state.services, 'id'),
  getPossibility: (state) => (serviceName) => state.possible.find((possibility) => possibility.service_name === serviceName),
  getPossibleInfo: (state, getters) => (serviceName) => getters.getPossibility(serviceName).setup_url,
  getPossibleProtocols: (state, getters) => (serviceName) => {
    const service = getters.getPossibility(serviceName)
    return [...new Set([...(service.protocols || []), ...(service.secure_protocols || [])])]
  },
}

const actions = {
  // one service
  async doPostService({ commit }, serviceName) {
    const result = await backend.secureAxios.post(`/notifications/services`, {
      type: serviceName,
    })
    commit(NOTI_SERVICE_CREATE, result.data)
  },
  // all services
  async doPutServices({ commit, getters }) {
    await backend.secureAxios.put(`/notifications/services`, {
      services: getters.getServices,
    })
    await commit(NOTI_SERVICE_TESTING_UPDATE, true)
    let testResult
    try {
      const testResponse = await backend.secureAxios.get(`/notifications/test_services`, getters.getServices)
      testResult = testResponse.data.result
    } catch (error) {
      // empty
    } finally {
      await commit(NOTI_SERVICE_TESTING_UPDATE, false)
    }
    Toast.open({
      message: testResult ? 'testing succeeded' : 'testing failed',
      type: testResult ? 'is-green' : 'is-primary',
    })
  },
  async doFetchServices({ commit }) {
    const result = await backend.secureAxios.get('/notifications/services')
    commit(NOTI_SERVICES_UPDATE, result.data)
  },
  // all possible
  async doFetchPossible({ commit }) {
    const result = await backend.secureAxios.get('/notifications/possible_services')
    commit(NOTI_POSSIBLE_UPDATE, result.data.schemas)
  },
  // strings
  async doFetchStrings({ commit }) {
    const result = await backend.secureAxios.get('/notifications/strings')
    commit(NOTI_STRINGS_UPDATE, result.data)
  },
  doPutStrings({ getters }) {
    backend.secureAxios.put('/notifications/strings', getters.getStrings)
  },
}

const mutations = {
  [NOTI_STRINGS_UPDATE](state, settings) {
    Vue.set(state, 'strings', settings)
  },
  [NOTI_STRING_UPDATE](state, { key, value }) {
    Vue.set(state.strings, key, value)
  },
  [NOTI_SERVICE_CREATE](state, service) {
    state.services.push(service)
  },
  [NOTI_SERVICES_UPDATE](state, settings) {
    Vue.set(state, 'services', settings)
  },
  [NOTI_SERVICE_UPDATE](state, { serviceID, key, value }) {
    const serviceIndex = state.services.findIndex((service) => service.id === serviceID)
    Vue.set(state.services[serviceIndex], key, value)
  },
  [NOTI_SERVICE_DELETE](state, serviceID) {
    state.services.splice(
      state.services.findIndex((service) => service.id === serviceID),
      1,
    )
  },
  [NOTI_POSSIBLE_UPDATE](state, services) {
    Vue.set(state, 'possible', services)
  },
  [NOTI_SERVICE_TESTING_UPDATE](state, value) {
    Vue.set(state, 'isTesting', value)
  },
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true,
}
