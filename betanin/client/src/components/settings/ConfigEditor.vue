<template lang="pug">
  div
    h5.title.is-5 config.yaml
    .control(
      :class="{ 'is-loading': isLoading }"
    )
      textarea.textarea.is-small.is-info.has-fixed-size(
        placeholder='hello'
        v-model='text'
        :disabled='wasError'
      )
    p(v-if='!wasError')
      | last read from disk at
      b  {{ readAt | formatTimestamp }}
    b-field(grouped group-multiline position='is-right')#buttons
      p.control
        button.button(
          @click='getConfig'
        ).is-light reload
      p.control
        button.button(
          @click='setConfig'
          :disabled='wasError'
        ).is-primary save
</template>

<script>
// import
import backend from '@/backend'
// help
const endpointPath = '/beets/config'
// export
export default {
  data () {
    return {
      text: '',
      readAt: '',
      isLoading: null
    }
  },
  methods: {
    setConfig () {
      backend.secureAxios.put(endpointPath,
        { config: this.text })
    },
    async getConfig () {
      this.isLoading = true
      try {
        const response = await backend.secureAxios.get(endpointPath)
        this.text = response.data.config
        this.readAt = response.data.time_read
      } catch (error) {
        this.text = `\
could not load config from backend.
reason: '${error.response.data.message}'`
        this.readAt = null
      }
      this.isLoading = false
    }
  },
  mounted () {
    this.getConfig()
  },
  computed: {
    wasError () {
      return this.readAt === null
    }
  }
}
</script>

<style scoped>
  #buttons {
    margin-top: 0.75rem;
  }
  textarea {
    border-radius: 4px !important;
    -webkit-border-radius: 4px !important;
    -moz-border-radius: 4px !important;
    border-radius: 5px !important;
    height: 100vh !important;
    font-family: monospace;
    background-color: #303030;
    color: #eee;
  }
  textarea:focus {
    border-color: unset;
    -webkit-box-shadow: unset;
    box-shadow: unset;
  }
</style>
