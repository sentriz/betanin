import Vue from 'vue'
import Router from 'vue-router'

import Settings from '@/components/Settings.vue'
import ModalConsole from '@/components/console/ModalConsole.vue'
import Torrents from '@/components/Torrents.vue'

Vue.use(Router)

export default new Router({
  linkActiveClass: 'is-active',
  routes: [
    {
      path: '/torrents/:listType',
      name: 'torrents',
      component: Torrents,
      children: [
        {
          path: 'console/:torrentID',
          name: 'modal console',
          components: {
            modal: ModalConsole
          },
          meta: {
            modalIsOpen: true
          }
        }
      ]
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings
    },
    {
      path: '*',
      redirect: '/torrents/active'
    }
  ]
})
