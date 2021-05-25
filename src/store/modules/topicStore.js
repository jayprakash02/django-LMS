import topicservice from '../../services/topicservice'

const state = {
  topics:[]
}

const getters = {
    topics: state => {
    return state.topics
  }
}

const actions = {
  getTopics ({ commit }) {
    topicservice.fetchTopics()
    .then(topics => {
      commit('setTopics', topics)
    })
  },
  searchTopics({commit},item){
    topicservice.searchTopics(item)
    .then(topics => {
      commit('setTopics',topics)
    })
  }
}

const mutations = {
    setTopics (state, topics) {
    state.topics = topics
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}