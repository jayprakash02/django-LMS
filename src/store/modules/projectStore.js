import projectService from '../../services/projectService'

const state = {
    projects:[]
}

const getters = {
    projects: state => {
    return state.projects
  }
}

const actions = {
  getProjects ({ commit }) {
    projectService.fetchProjects()
    .then(projects => {
      commit('setProjects', projects)
    })
  },
  searchProjects({commit},item){
    projectService.searchProjects(item)
    .then(projects => {
      commit('setProjects',projects)
    })
  }
}

const mutations = {
    setProjects (state, projects) {
    state.projects = projects
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}