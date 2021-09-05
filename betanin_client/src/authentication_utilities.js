// this module only exists to fix a circular import

export default {
  clearToken() {
    delete localStorage.token
  },
  setToken(token) {
    localStorage.token = token
  },
  getToken() {
    return localStorage.token
  },
  isLoggedIn() {
    return localStorage.token !== undefined
  },
}
