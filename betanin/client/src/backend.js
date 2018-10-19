import axios from 'axios'
import { Toast } from 'buefy/dist/components/toast'
import { API_URL } from './app_constants'

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// request intercept
// $axios.interceptors.request.use(
// )

// response intercept
$axios.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    Toast.open({
      message: 'network error',
      type: 'is-primary'
    })
    return Promise.reject(error)
  }
)

export default {
  fetchResource (route) {
    return $axios.get(route)
      .then(response => response.data)
  },
  putResource (route, data) {
    return $axios.put(route, data)
      .then(response => response.data)
  },
  postResource (route, data) {
    return $axios.post(route, data)
      .then(response => response.data)
  },
  deleteResource (route) {
    return $axios.delete(route)
      .then(response => response.data)
  }
}
