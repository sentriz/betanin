const lastN = (list, n) =>
  typeof n === 'undefined'
    ? list
    : list.slice(-n)

const itemFromID = (items, id) =>
  items.find(item =>
    item.id === id
  )

export default {
  torrentsActivity: state =>
    state.torrents.filter(item =>
      item.status !== 'COMPLETED'),
  torrentsHistory: state =>
    state.torrents.filter(item =>
      item.status === 'COMPLETED'),
  notificationSettingsGeneral: state =>
    state.notificationSettingsGeneral,
  notificationSettingsServices: state =>
    state.notificationSettingsServices,
  notificationSettingsPossibleServices: state =>
    state.notificationSettingsPossibleServices,
  serviceFromID: state => serviceID =>
    itemFromID(state.notificationSettingsServices, serviceID),
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
    itemFromID(state.torrents, torrentID)
}
