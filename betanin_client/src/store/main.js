import Vue from "vue";
import Vuex from "vuex";

import torrents from "./modules/torrents";
import lines from "./modules/lines";
import notifications from "./modules/notifications";
import status from "./modules/status";

Vue.use(Vuex);

export default new Vuex.Store({
  strict: process.env.NODE_ENV !== "production",
  modules: {
    torrents,
    lines,
    notifications,
    status,
  },
});
