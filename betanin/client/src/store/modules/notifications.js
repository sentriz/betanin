import Vue from 'vue'
import backend from '@/backend'
import {
  NOTI_GENERALS_UPDATE,
  NOTI_GENERAL_UPDATE,
  NOTI_POSSIBLE_UPDATE,
  NOTI_SERVICES_UPDATE,
  NOTI_SERVICE_CREATE,
  NOTI_SERVICE_DELETE,
  NOTI_SERVICE_UPDATE
} from '../mutation-types'
import { itemFromID } from '../utilities'

const state = {
  general: {},
  services: [],
  possible: []
}

const getters = {
  getGeneral: state =>
    state.general,
  getPossible: state =>
    state.possible,
  getServices: state =>
    state.services,
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
  doPostService ({ commit }, serviceName) {
    backend.postResource(
      `settings/notifications/services`,
      { type: serviceName }
    ).then(result => {
      commit(NOTI_SERVICE_CREATE, result)
    })
  },
  // all services
  doPutServices ({ commit, getters }) {
    backend.putResource(
      `settings/notifications/services`,
      getters.getServices
    )
  },
  doFetchServices ({ commit }) {
    backend.fetchResource('settings/notifications/services')
      .then(result => {
        commit(NOTI_SERVICES_UPDATE, result)
      })
  },
  // all possible
  doFetchPossible ({ commit }) {
    backend.fetchResource('settings/notifications/possible_services')
      .then(result => {
        commit(NOTI_POSSIBLE_UPDATE, result.schemas)
      })
  },
  // general
  doFetchGeneral ({ commit }) {
    backend.fetchResource('settings/notifications/general')
      .then(result => {
        commit(NOTI_GENERALS_UPDATE, result)
      })
  },
  doPutGeneral ({ commit, getters }) {
    backend.putResource(
      'settings/notifications/general',
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
      state.services.findIndex(service => service.id === serviceID), 1
    )
  },
  [NOTI_POSSIBLE_UPDATE] (state, services) {
    Vue.set(state, 'possible', services)
  }
}

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true

}
