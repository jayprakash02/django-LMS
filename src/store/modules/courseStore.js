import courseService from '../../services/courseService'

const state = {
  courses:[]
}

const getters = {
    courses: state => {
    return state.courses
  }
}

const actions = {
  getCourses ({ commit }) {
    courseService.fetchCourses()
    .then(courses => {
      commit('setCourses', courses)
    })
  }
}

const mutations = {
    setCourses (state, courses) {
    state.courses = courses
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}