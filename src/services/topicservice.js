import api from '@/services/api'

export default {
  fetchTopics() {
    return api.get(`tag/`)
      .then(response => response.data)
  },
  searchTopics(item) {
    return api.get(`tag/?search=${item}`)
      .then(response => response.data)
  }
}