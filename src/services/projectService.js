import api from '@/services/api'

export default {
  fetchProjects() {
    return api.get(`project/`)
              .then(response => response.data)
  },
  searchProjects(item) {
    return api.get(`project/?search=${item}`)
      .then(response => response.data)
  }
}