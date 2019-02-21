import backend from '@/backend'
import authUtils from '@/authentication_utilities'
import router from '@/router'

export default {
  async login (username, password) {
    try {
      const response = await backend.insecureAxios.post(
        'authentication/login',
        { username, password }
      )
      authUtils.setToken(response.data.token)
      router.replace(router.currentRoute.query.redirect || '/')
    } catch (error) {
      if (error.response !== undefined && error.response.status === 422) {
        return error.response.data.message
      } else {
        return 'unexpected error while fetching a token from the backend'
      }
    }
  },
  logout (redirect) {
    authUtils.clearToken()
    router.replace({
      name: 'login',
      query: { redirect }
    })
  }
}
