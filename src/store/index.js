import Vue from 'vue'
import Vuex from 'vuex'

import courses from '@/store/modules/courseStore.js'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    courses,
  }
})