import Vue from "vue";
import backend from "@/backend";
import { cleanObject } from "../utilities";
import {
  STATUS_CONNECTED_UPDATE,
  STATUS_SYSTEM_UPDATE,
} from "../mutation-types";

const state = {
  connected: false,
  systemInfo: {},
};

const getters = {
  getConnected: (state) => state.connected,
  getSystemInfo: (state) => state.systemInfo,
};

const actions = {
  doSocket__connect: ({ commit }) => {
    commit(STATUS_CONNECTED_UPDATE, true);
  },
  doSocket__disconnect: ({ commit }) => {
    commit(STATUS_CONNECTED_UPDATE, false);
  },
  async doFetchSystemInfo({ commit }) {
    const result = await backend.secureAxios.get("/meta/system_info");
    const cleanInfo = cleanObject(result.data);
    commit(STATUS_SYSTEM_UPDATE, cleanInfo);
  },
};

const mutations = {
  [STATUS_CONNECTED_UPDATE](state, connected) {
    Vue.set(state, "connected", connected);
  },
  [STATUS_SYSTEM_UPDATE](state, info) {
    Vue.set(state, "systemInfo", info);
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
  namespaced: true,
};
