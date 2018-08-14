import axios from 'axios'

const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const API_URL = IS_PRODUCTION ? '/api/' : 'http://localhost:5000/api/'

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

// Request Interceptor
$axios.interceptors.request.use(
  function (config) {
    config.headers['Authorization'] = 'Fake Token'
    return config
  }
)

// Response Interceptor to handle and log errors
$axios.interceptors.response.use(
  function (response) {
    return response
  },
  function (error) {
    console.log(error)
    return Promise.reject(error)
  }
)

export default {
  fetchResource (route) {
    return $axios.get(route)
      .then(response => response.data)
  }
}
