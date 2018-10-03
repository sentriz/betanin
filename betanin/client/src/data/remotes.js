const remoteNames = [
  'Transmission'
]

export default remoteNames.map(remote => ({
  name: remote.toLowerCase(),
  component: () => import(`@/components/remote/${remote}`)
}))
