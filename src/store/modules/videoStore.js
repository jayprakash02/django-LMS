import videoService from '../../services/videoService'

const state = {
  videos:[]
}

const getters = {
    posts: state => {
    return state.videos
  }
}

const actions = {
  getVideos ({ commit }) {
    videoService.fetchVideos()
    .then(videos => {
      commit('setVideos', videos)
    })
  }
}

const mutations = {
  setVideos (state, videos) {
    state.videos = videos
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}