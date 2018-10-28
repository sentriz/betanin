const lastN = (list, n) =>
  typeof n === 'undefined'
    ? list
    : list.slice(-n)

const itemFromID = (items, id) =>
  items.find(item =>
    item.id === id
  )

export default {
  downloadsActivity: state =>
    state.downloads.filter(item =>
      item.status !== 'COMPLETED'),
  downloadsHistory: state =>
    state.downloads.filter(item =>
      item.status === 'COMPLETED'),
  status: state =>
    state.status,
  lines: state => (torrentID, lineLimit) =>
    lastN(state.lines[torrentID] || [], lineLimit),
  areLines: state => torrentID =>
    Boolean(state.lines[torrentID]),
  linesFetched: state => torrentID =>
    state.fetchedLines.includes(torrentID),
  connected: state =>
    state.connected,
  torrent: state => torrentID =>
    itemFromID(state.downloads, torrentID)
}
