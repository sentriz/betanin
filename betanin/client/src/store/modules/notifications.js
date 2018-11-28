import Vue from 'vue'
import backend from '@/backend'
import { NOTI_SERVICE_CREATE,
  NOTI_POSSIBLE_UPDATE,
  NOTI_SERVICES_UPDATE,
  NOTI_SERVICE_UPDATE,
  NOTI_SERVICE_DELETE
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
  getServices: state =>
    state.services,
  getPossible: state =>
    state.possible,
  getServiceFromID: state => serviceID =>
    itemFromID(state.services, serviceID)
}

const actions = {
  doFetchPossible ({ commit }) {
    backend.fetchResource('settings/notifications/possible_services')
      .then(result => {
        commit(NOTI_POSSIBLE_UPDATE, result.schemas)
      })
  },
  doFetchServices ({ commit }) {
    backend.fetchResource('settings/notifications/services')
      .then(result => {
        commit(NOTI_SERVICES_UPDATE, result)
      })
  },
  doDeleteService ({ commit }, serviceID) {
    backend.deleteResource(`settings/notifications/services/${serviceID}`)
      .then(result => {
        commit(NOTI_SERVICE_DELETE, serviceID)
      })
  },
  doPutService ({ commit, getters }, serviceID) {
    const service = getters.getServiceFromID(serviceID)
    backend.putResource(
      `settings/notifications/services/${serviceID}`,
      service
    )
  },
  doPostService ({ commit }, serviceType) {
    backend.postResource(
      `settings/notifications/services`,
      { type: serviceType }
    ).then(result => {
      commit(NOTI_SERVICE_CREATE, result)
    })
  },
  socket_connect: ({ dispatch }) => {
    dispatch('doFetchServices')
    dispatch('doFetchPossible')
  }
}

const mutations = {
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
