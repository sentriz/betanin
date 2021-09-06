<template lang="pug">
.search
  b-field.import-label(label='manually import')
  b-field
    b-autocomplete(
      v-model='selection',
      expanded,
      placeholder='eg. /downloads/music/the fall - dragnet (1979)',
      :data='results',
      @typing='manualFind'
    )
      template(slot='empty')
        p no results found
    p.control
      button.button(@click='doImport')
        b-icon.import-button(icon='folder-multiple-plus')
</template>

<script>
// import
import debounce from 'lodash.debounce'
import backend from '@/backend'
import { ToastProgrammatic as Toast } from 'buefy'
// export
export default {
  data() {
    return {
      results: [],
      selection: '',
    }
  },
  methods: {
    async doImport() {
      const fetchUrl = `torrents`
      const formData = new FormData()
      formData.append('both', this.selection)
      try {
        await backend.secureAxios.post(fetchUrl, formData)
      } catch (error) {
        Toast.open({
          message: `error importing: ${error.response.data.message}`,
          type: 'is-primary',
        })
      } finally {
        this.selection = ''
      }
    },
    manualFind: debounce(async function async(dir) {
      if (!dir.length) {
        this.results = []
        return
      }
      const results = await backend.secureAxios.get(`/meta/sub_dirs`, {
        params: { dir },
      })
      this.results = []
      for (let item of results.data) {
        this.results.push(item.path)
      }
    }, 200),
  },
}
</script>

<style lang="scss" scoped>
.search {
  .import-button {
    margin: 0 0.5rem;
  }
  .import-label {
    margin-bottom: 8px;
  }
}
</style>
