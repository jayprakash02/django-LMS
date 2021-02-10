import api from '@/services/api'

export default {
  fetchProjects() {
    return api.get(`project/`)
              .then(response => response.data)
  },
}