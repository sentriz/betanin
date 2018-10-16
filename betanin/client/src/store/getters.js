const lastN = (list, n) =>
  typeof n === 'undefined'
    ? list
    : list.slice(-n)

const itemFromID = (items, id) =>
  items.find(item =>
    item.id === id
  )

export default {
  downloads: state =>
    state.downloads,
  status: state =>
    state.status,
  lines: state => (torrentID, lineLimit) =>
    lastN(state.lines[torrentID] || [], lineLimit),
  areLines: state => torrentID =>
    Boolean(state.lines[torrentID]),
  connected: state =>
    state.connected,
  haveDownloads: state =>
    state.downloads.length !== 0,
  torrent: state => torrentID =>
    itemFromID(state.downloads, torrentID),
  remotes: state =>
    state.remotes,
  remoteIDs: state =>
    state.remotes.map(remote => remote.id),
  remoteFromID: state => remoteID =>
    itemFromID(state.remotes, remoteID),
  remoteConfigFromID: state => remoteID =>
    itemFromID(state.remotes, remoteID).config,
  remoteTypeFromID: state => remoteID =>
    itemFromID(state.remotes, remoteID).type
}
