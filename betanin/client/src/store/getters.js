const lastN = (list, n) =>
  typeof n === 'undefined'
    ? list
    : list.slice(-n)

export default {
  downloads: state =>
    state.downloads,
  lines: state => (torrentID, lineLimit) =>
    lastN(state.lines[torrentID] || [], lineLimit),
  areLines: state => torrentID =>
    Boolean(state.lines[torrentID]),
  connected: state =>
    state.connected,
  haveDownloads: state =>
    state.downloads.length !== 0,
  torrent: state => torrentID =>
    state.downloads.find(torrent =>
      torrent.id === torrentID
    ),
  remoteIDs: state =>
    state.remotes.map(remote =>
      remote.id
    ),
  remotes: state =>
    state.remotes,
  remote: state => remoteID =>
    state.remotes.find(remote =>
      remote.id === remoteID
    )
}
