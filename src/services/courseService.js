import api from '@/services/api'

export default {
  fetchCourses() {
    return api.get(`course/`)
              .then(response => response.data)
  },
}