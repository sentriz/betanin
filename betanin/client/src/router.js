import Vue from 'vue'
import Router from 'vue-router'

import Settings from '@/components/Settings.vue'
import ModalConsole from '@/components/console/ModalConsole.vue'
import Torrents from '@/components/Torrents.vue'
import Login from '@/views/Login.vue'
import Betanin from '@/views/Betanin.vue'
import authUtils from '@/authentication_utilities'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'is-active',
  routes: [
    {
      name: 'login',
      path: '/login',
      component: Login
    },
    {
      name: 'betanin',
      path: '/',
      redirect: {
        name: 'torrents',
        params: { listType: 'active' }
      },
      component: Betanin,
      children: [
        {
          path: 'torrents/:listType',
          name: 'torrents',
          component: Torrents,
          beforeEnter: requireAuth,
          children: [
            {
              path: 'console/:torrentID',
              name: 'modal console',
              components: { modal: ModalConsole },
              meta: { modalIsOpen: true }
            }
          ]
        },
        {
          path: 'settings',
          name: 'settings',
          component: Settings,
          beforeEnter: requireAuth
        }
      ]
    },
    {
      path: '*',
      redirect: '/'
    }
  ]
})

function requireAuth (to, from, next) {
  if (!authUtils.isLoggedIn()) {
    next({
      name: 'login',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}
