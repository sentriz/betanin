import store from '@/store/store'

export const genComputed = key => ({
  get () {
    const service = store.getters.serviceFromID(this.serviceID)
    return service[key]
  },
  set (value) {
    store.commit('updateServiceConfig', {
      serviceID: this.serviceID,
      key,
      value
    })
  }
})
