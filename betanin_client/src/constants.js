const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const LOCAL_PROTOCOL = 'http://'
const LOCAL_HOSTNAME = 'localhost'
const LOCAL_PORT = 9393
const PATH = '/api'

export const SOCKET_URL = IS_PRODUCTION ? '/' : LOCAL_PROTOCOL + LOCAL_HOSTNAME + ':' + LOCAL_PORT

export const API_URL = IS_PRODUCTION ? PATH : LOCAL_PROTOCOL + LOCAL_HOSTNAME + ':' + LOCAL_PORT + PATH
