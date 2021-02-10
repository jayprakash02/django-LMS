import api from '@/services/api'

export default {
  fetchVideos() {
    return api.get(`video/`)
              .then(response => response.data)
  },
}