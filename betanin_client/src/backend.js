import auth from '@/authentication'
import authUtils from '@/authentication_utilities'
import axios from 'axios'
import { API_URL } from '@/constants'
import router from '@/router'

const baseAxios = {
  baseURL: API_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json',
  },
}

const insecureAxios = axios.create(baseAxios)
const secureAxios = axios.create(baseAxios)
secureAxios.interceptors.request.use((config) => {
  config.headers['Authorization'] = `Bearer ${authUtils.getToken()}`
  return config
}, undefined)
secureAxios.interceptors.response.use(undefined, (error) => {
  if (error.response !== undefined && error.response.status === 401 && router.currentRoute.path !== '/login') {
    // the token has expired. get a new one
    auth.logout(router.currentRoute.fullPath)
  }
  return Promise.reject(error)
})

export default {
  insecureAxios,
  secureAxios,
}
