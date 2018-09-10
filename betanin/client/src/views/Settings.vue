      <!-- b-icon(icon='menu-down') -->
<template lang="pug">
  b-dropdown(hoverable)
    button.button.is-info(slot='trigger')
      span {{ remote }}
      span &nbsp;v
    b-dropdown-item(
      v-for='remote in remotes'
      :key='remote'
    ) {{ remote }}
</template>

<script>
const defaultRemote = 'transmission'
export default {
  data () {
    return {
      remote: defaultRemote,
      remotes: [
        defaultRemote,
        'deluge',
        'rtorrent'
      ]
    }
  }
}
</script>
