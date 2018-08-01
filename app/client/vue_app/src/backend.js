import axios from 'axios'
import { Toast } from 'buefy'

const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const API_URL = IS_PRODUCTION ? '/api/' : 'http://localhost:5000/api/'

let $axios = axios.create({
  baseURL: API_URL,
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
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
      message: error.message,
      type: 'is-danger'
    })
    return Promise.reject(error)
  }
)

export default {
  fetchResource (route) {
    return $axios.get(route)
      .then(response => response.data)
  }
}
