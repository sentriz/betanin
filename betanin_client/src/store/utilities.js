/* eslint-disable no-multi-spaces, key-spacing, complexity */
export const binaryInsert = (array, item, start, end) => {
  start ??= 0
  end ??= array.length - 1

  const middle = start + Math.floor((end - start) / 2)
  if (array.length === 0) array.push(item)
  else if (item.index > array[end].index) array.splice(end + 1, 0, item)
  else if (item.index < array[start].index) array.splice(start, 0, item)
  else if (item.index < array[middle].index) binaryInsert(array, item, start, middle - 1)
  else if (item.index > array[middle].index) binaryInsert(array, item, middle + 1, end)
}

export const cleanObject = (object) => {
  const knownMap = {
    torrent_id: 'torrentID',
  }
  for (const [key, value] of Object.entries(object)) {
    // fix known fixes
    if (key in knownMap) {
      delete object[key]
      object[knownMap[key]] = value
      continue
    }
    // try to fix others
    const newKey = key.replace(/(_\w)/g, (m) => m[1].toUpperCase())
    if (key === newKey) {
      continue
    }
    delete object[key]
    object[newKey] = value
  }
  return object
}
