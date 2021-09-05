import Vue from "vue";
import Router from "vue-router";
import authUtils from "@/authentication_utilities";

import Betanin from "@/views/Betanin.vue";
import Login from "@/views/Login.vue";

import ConfigEditor from "@/components/settings/ConfigEditor.vue";
import ModalConsole from "@/components/console/ModalConsole.vue";
import NotificationEditor from "@/components/settings/NotificationEditor.vue";
import Settings from "@/components/Settings.vue";
import TorrentClients from "@/components/settings/TorrentClients.vue";
import Torrents from "@/components/Torrents.vue";

Vue.use(Router);

const requireAuth = (to, from, next) => {
  if (authUtils.isLoggedIn()) {
    next();
    return;
  }
  next({
    name: "login",
    query: { redirect: to.fullPath },
  });
};

const pages = [
  {
    path: "torrents",
    name: "torrents",
    component: Torrents,
    beforeEnter: requireAuth,
    children: [
      {
        path: "console/:torrentID",
        name: "modal console",
        components: { modal: ModalConsole },
        meta: { modalIsOpen: true },
      },
    ],
  },
  {
    path: "settings",
    component: Settings,
    beforeEnter: requireAuth,
    children: [
      {
        path: "clients",
        component: TorrentClients,
      },
      {
        path: "notifications",
        component: NotificationEditor,
      },
      {
        path: "beets",
        component: ConfigEditor,
      },
      {
        name: "settings",
        path: "",
        redirect: "clients",
      },
    ],
  },
];

const screens = [
  {
    name: "login",
    path: "/login",
    component: Login,
  },
  {
    name: "betanin",
    path: "/",
    redirect: {
      name: "torrents",
    },
    component: Betanin,
    children: pages,
  },
  {
    path: "*",
    redirect: "/",
  },
];

export default new Router({
  linkActiveClass: "is-active",
  routes: screens,
});
