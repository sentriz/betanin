import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'
import './filters'

import Buefy from 'buefy'
import 'buefy/lib/buefy.css'

Vue.use(Buefy)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
