export const lastN = (list, n) =>
  typeof n === 'undefined'
    ? list
    : list.slice(-n)

export const itemFromID = (items, id) =>
  items.find(item =>
    item.id === id
  )

/* eslint-disable no-multi-spaces, key-spacing, complexity */
export const binaryInsert = (array, item, startVal, endVal) => {
  const value  = Number(item.index)
  const length = array.length
  const start  = typeof startVal !== 'undefined' ? startVal : 0
  const end    = typeof endVal   !== 'undefined' ? endVal   : length - 1
  const middle = start + Math.floor((end - start) / 2)
  if      (length === 0)                array.push(item)
  else if (value > array[end].index)    array.splice(end + 1, 0, item)
  else if (value < array[start].index)  array.splice(start, 0, item)
  else if (value < array[middle].index) binaryInsert(array, item, start, middle - 1)
  else if (value > array[middle].index) binaryInsert(array, item, middle + 1, end)
}
