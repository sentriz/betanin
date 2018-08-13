import Vue from 'vue'
import Buefy from 'buefy'
import VueSocketio from 'vue-socket.io-extended'
import IO from 'socket.io-client'

import App from './App.vue'
import router from './router'
import store from './store'
import { SOCKET_URL } from './backend'
import './filters'

import 'buefy/lib/buefy.css'
import 'font-awesome/css/font-awesome.min.css'

Vue.use(
  Buefy,
  {
    defaultIconPack: 'fa',
    defaultContainerElement: 'app'
  }
)
Vue.use(
  VueSocketio,
  IO(SOCKET_URL),
  { store }
)
Vue.config.productionTip = false

const view = new Vue({
  router,
  store,
  render: h => h(App)
})
view.$mount('#app')
