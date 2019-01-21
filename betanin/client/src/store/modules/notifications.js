import Vue from 'vue'
import backend from '@/backend'
import {
  NOTI_GENERALS_UPDATE,
  NOTI_GENERAL_UPDATE,
  NOTI_POSSIBLE_UPDATE,
  NOTI_SERVICES_UPDATE,
  NOTI_SERVICE_CREATE,
  NOTI_SERVICE_DELETE,
  NOTI_SERVICE_UPDATE,
  NOTI_SERVICE_TESTING_UPDATE
} from '../mutation-types'
import { itemFromID } from '../utilities'
import { Toast } from 'buefy/dist/components/toast'

const state = {
  general: {},
  services: [],
  possible: [],
  isTesting: false
}

const getters = {
  getGeneral: state =>
    state.general,
  getPossible: state =>
    state.possible,
  getServices: state =>
    state.services,
  getIsTesting: state =>
    state.isTesting,
  getServiceFromID: state => serviceID =>
    itemFromID(state.services, serviceID),
  getPossibility: state => serviceName => state.possible.find(
    possibility => possibility.service_name === serviceName),
  getPossibleInfo: (state, getters) => serviceName =>
    getters.getPossibility(serviceName).setup_url,
  getPossibleProtocols: (state, getters) => serviceName => {
    const service = getters.getPossibility(serviceName)
    return [...new Set([
      ...service.protocols || [],
      ...service.secure_protocols || []
    ])]
  }
}

const actions = {
  // one service
  async doPostService ({ commit }, serviceName) {
    const result = await backend.postResource(
      `/notifications/services`,
      { type: serviceName }
    )
    commit(NOTI_SERVICE_CREATE, result)
  },
  // all services
  async doPutServices ({ commit, getters }) {
    await backend.putResource(
      `/notifications/services`,
      { services: getters.getServices }
    )
    await commit(NOTI_SERVICE_TESTING_UPDATE, true)
    let testResult
    try {
      const testResponse = await backend.fetchResource(
        `/notifications/test_services`,
        getters.getServices
      )
      testResult = testResponse.result
    } catch (error) {
    } finally {
      await commit(NOTI_SERVICE_TESTING_UPDATE, false)
    }
    Toast.open({
      message: testResult ? 'testing succeeded' : 'testing failed',
      type: testResult ? 'is-green' : 'is-primary'
    })
  },
  async doFetchServices ({ commit }) {
    const result = await backend.fetchResource(
      '/notifications/services')
    commit(NOTI_SERVICES_UPDATE, result)
  },
  // all possible
  async doFetchPossible ({ commit }) {
    const result = await backend.fetchResource(
      '/notifications/possible_services')
    commit(NOTI_POSSIBLE_UPDATE, result.schemas)
  },
  // general
  async doFetchGeneral ({ commit }) {
    const result = await backend.fetchResource(
      '/notifications/general')
    commit(NOTI_GENERALS_UPDATE, result)
  },
  doPutGeneral ({ getters }) {
    backend.putResource(
      '/notifications/general',
      getters.getGeneral
    )
  }
}

const mutations = {
  [NOTI_GENERALS_UPDATE] (state, settings) {
    Vue.set(state, 'general', settings)
  },
  [NOTI_GENERAL_UPDATE] (state, { key, value }) {
    Vue.set(state.general, key, value)
  },
  [NOTI_SERVICE_CREATE] (state, service) {
    state.services.push(service)
  },
  [NOTI_SERVICES_UPDATE] (state, settings) {
    Vue.set(state, 'services', settings)
  },
  [NOTI_SERVICE_UPDATE] (state, { serviceID, key, value }) {
    const serviceIndex = state.services.findIndex(service =>
      service.id === serviceID
    )
    Vue.set(state.services[serviceIndex], key, value)
  },
  [NOTI_SERVICE_DELETE] (state, serviceID) {
    state.services.splice(
      state.services.findIndex(service =>
        service.id === serviceID), 1
    )
  },
  [NOTI_POSSIBLE_UPDATE] (state, services) {
    Vue.set(state, 'possible', services)
  },
  [NOTI_SERVICE_TESTING_UPDATE] (state, value) {
    Vue.set(state, 'isTesting', value)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true

}
