import store from '@/store/main'
import {
  NOTI_SERVICE_UPDATE,
  NOTI_STRING_UPDATE
} from '@/store/mutation-types'

export const genNotiServiceComputed = key => ({
  get () {
    const getter = store.getters['notifications/getServiceFromID']
    const service = getter(this.serviceID)
    return service[key]
  },
  set (value) {
    store.commit(`notifications/${NOTI_SERVICE_UPDATE}`, {
      serviceID: this.serviceID,
      key,
      value
    })
  }
})

export const genNotiStringsComputed = key => ({
  get () {
    const getter = store.getters['notifications/getStrings']
    return getter[key]
  },
  set (value) {
    store.commit(`notifications/${NOTI_STRING_UPDATE}`, {
      key,
      value
    })
  }
})
