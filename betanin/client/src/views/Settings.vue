<template lang="pug">
  .box
    b-field(
      horizontal
      label='remote'
    )
      b-select(
        :placeholder='remoteName'
        v-model='remoteName'
      )
        option(
          v-for='remote in remotes'
          :value='remote.name'
        ) {{ remote.name }}
    component(
      :is='remote.component'
      v-if='remote'
    )
</template>

<script>
// imports
import remotes from '@/data/remotes'
// export
export default {
  methods: {
    setRemote (remote) {
      console.log(remote)
      this.remote = remote
    }
  },
  computed: {
    remote () {
      return remotes.find(remote =>
        remote.name === this.remoteName
      )
    }
  },
  data () {
    return {
      remotes: remotes,
      remoteName: 'transmission'
    }
  }
}
</script>

<style scoped>
  #buttons {
    padding-top: 12px;
  }
</style>
