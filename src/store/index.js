import Vue from 'vue'
import Vuex from 'vuex'

import courses from '@/store/modules/courseStore.js'
import projects from '@/store/modules/projectStore.js'
import videos from '@/store/modules/videoStore.js'
Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    courses,projects,videos
  }
})