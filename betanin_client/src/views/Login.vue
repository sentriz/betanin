<template lang='pug'>
  .container
    .card
      img#logo(
        :src='require("../assets/logo.png")'
      )
      #form
        b-field(
          :type='{"is-primary": errors.has("username")}'
          :message='errors.first("username")'
        )
          b-input(
            icon='account'
            placeholder='username'
            v-model='username'
            v-validate="'required'"
            data-vv-name='username'
          )
        b-field(
          :type='{"is-primary": errors.has("password")}'
          :message='errors.first("password")'
        )
          b-input(
            icon='lock'
            placeholder='password'
            v-model='password'
            type='password'
            v-validate="'required'"
            data-vv-name='password'
            password-reveal
            @keyup.native.enter='login'
          )
        button.button.is-primary.is-pulled-right(
          @click='login'
        ) login
        center
          p#error-text(v-if='errorMessage') {{ errorMessage }}
</template>

<script>
import auth from '@/authentication'
export default {
  data () {
    return {
      username: '',
      password: '',
      errorMessage: ''
    }
  },
  methods: {
    async login () {
      const isValid = await this.$validator.validateAll()
      if (!isValid) {
        return
      }
      this.errorMessage = await auth.login(this.username, this.password)
    }
  }
}
</script>

<style lang='scss' scoped>
  .container {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .error {
    color: red;
  }
  .card {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 1rem;
    max-width: 560px;
    #form {
      width: 100%;
    }
    #logo {
      width: 45%;
    }
    > * {
      margin: 1.5rem 0;
    }
  }
  #error-text {
    color: #696969;
    margin-top: 18px;
  }
</style>
