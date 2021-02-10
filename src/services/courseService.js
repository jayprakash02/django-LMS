import api from '@/services/api'

export default {
  fetchCourses() {
    return api.get(`course/`)
      .then(response => response.data)
  },
  searchCourses(item) {
    return api.get(`course/?search=${item}`)
      .then(response => response.data)
  }
}