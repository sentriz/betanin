<template lang="pug">
.container
  .card
    img#logo(:src="require('../assets/logo.png')")
    validation-observer#form(v-slot="{ handleSubmit }")
      validation-provider(
        name="username",
        rules="required",
        v-slot="{ errors }",
        slim
      )
        b-field(:type="{ 'is-primary': errors.length }", :message="errors[0]")
          b-input(icon="account", placeholder="username", v-model="username")
      validation-provider(
        name="password",
        rules="required",
        v-slot="{ errors }",
        slim
      )
        b-field(:type="{ 'is-primary': errors.length }", :message="errors[0]")
          b-input(
            icon="lock",
            placeholder="password",
            v-model="password",
            type="password",
            password-reveal,
            @keyup.native.enter="login"
          )
      button.button.is-primary.is-pulled-right(@click="handleSubmit(login)") login
</template>

<script>
import { ValidationProvider, ValidationObserver } from "vee-validate";
import { ToastProgrammatic as Toast } from "buefy";
import auth from "@/authentication";
export default {
  components: { ValidationProvider, ValidationObserver },
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      const message = await auth.login(this.username, this.password);
      if (!message) return;
      Toast.open({
        message,
        type: "is-primary",
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.container {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.card {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  padding: 2rem;
  max-width: 420px;
  #form {
    width: 100%;
    margin-top: 26px;
  }
  #logo {
    width: 60%;
  }
}
</style>
