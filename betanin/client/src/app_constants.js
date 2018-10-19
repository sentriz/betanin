const PROTOCOL = 'http://'
const HOSTNAME = 'localhost'
const PORT = 5000
const PATH = '/api'
const IS_PRODUCTION = process.env.NODE_ENV === 'production'

export const SOCKET_URL = IS_PRODUCTION
  ? '/'
  : PROTOCOL + HOSTNAME + ':' + PORT

export const API_URL = IS_PRODUCTION
  ? PATH
  : PROTOCOL + HOSTNAME + ':' + PORT + PATH
