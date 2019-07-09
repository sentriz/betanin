<template lang="pug">
  div
    h5.title.is-5 api key
    code {{ apiKey }}
    hr
    .title.is-5 script examples
    .columns
      .column
        .title.is-7.example-heading transmission
        pre
          | <u><a href="https://github.com/transmission/transmission/wiki/Scripts#On_Torrent_Completion"># torrent-finished.sh</a></u>
          |
          | #!/bin/sh
          |
          | curl \
          |     --request POST \
          |     --data-urlencode "path=/mnt/media/downloads" \
          |     --data-urlencode "name=$TR_TORRENT_NAME" \
          |     --header "X-API-Key: <b>{{ apiKey }}</b>" \
          |     "<b>{{ origin }}</b>/api/torrents"
        br
        pre
          | <u><a href="https://github.com/transmission/transmission/wiki/Editing-Configuration-Files"># settings.json (excerpt)</a></u>
          |
          | ...
          | "script-torrent-done-enabled": <b>true</b>,
          | "script-torrent-done-filename": <b>"/path/to/above/finished.sh"</b>,
          | ...
      .column
        .title.is-7.example-heading deluge
        pre
          | <u># torrent-finished.sh</u>
          |
          | #!/bin/sh
          |
          | coming soon
</template>

<script>
import backend from '@/backend'
export default {
  data () {
    return {
      apiKey: 'loading...'
    }
  },
  computed: {
    origin () {
      return window.location.origin
    }
  },
  async mounted () {
    const response = await backend.secureAxios.get('clients/api_key')
    this.apiKey = response.data.api_key
  }
}
</script>

<style>
  .example-heading {
    margin-bottom: 0.45rem !important;
    color: #888 !important;
  }
</style>
