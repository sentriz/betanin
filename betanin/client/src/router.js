import Vue from 'vue'
import Router from 'vue-router'

import Activity from './views/Activity.vue'
import History from './views/History.vue'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'is-active',
  routes: [
    {
      path: '/activity',
      name: 'activity',
      component: Activity
    },
    {
      path: '/history',
      name: 'history',
      component: History
    },
    {
      path: '*',
      redirect: '/activity'
    }
  ]
})
