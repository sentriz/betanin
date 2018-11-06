<template lang="pug">
  div
    .control(
      :class="{ 'is-loading': isLoading }"
    )
      textarea.textarea.is-small.is-info.has-fixed-size(
        placeholder='hello'
        v-model='text'
      )
    b-field(grouped group-multiline position='is-right')#buttons
      p.control
        button.button(@click='reloadConfig').is-light reload
      p.control
        button.button(@click='setConfig').is-primary save
</template>

<script>
// import
import backend from '@/backend'
import { Toast } from 'buefy/dist/components/toast'
// help
const endpointPath = 'settings/beets/config'
// export
export default {
  data () {
    return {
      text: '',
      isLoading: null
    }
  },
  methods: {
    setConfig () {
      backend.putResource(endpointPath, this.text)
    },
    getConfig () {
      this.isLoading = true
      backend.fetchResource(endpointPath)
        .then(text => {
          this.text = text
          this.isLoading = false
        })
    },
    reloadConfig () {
      this.getConfig()
      Toast.open({
        message: 'config loaded from disk',
        type: 'is-green'
      })
    }
  },
  mounted () {
    this.getConfig()
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
