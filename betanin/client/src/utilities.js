import store from '@/store/store'

export const genComputed = key => ({
  get () {
    const remote = store.getters.remote(this.remoteID)
    return remote.config[key]
  },
  set (value) {
    store.commit('updateRemoteConfig', {
      remoteID: this.remoteID,
      key,
      value
    })
  }
})
