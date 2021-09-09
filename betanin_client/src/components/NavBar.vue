<template lang="pug">
nav.navbar
  .navbar-brand
    router-link.brand-link.navbar-item(to='/')
      img.logo(:src='getLogoPath()', height='100%')
    a.navbar-burger(role='button', @click='toggleShow', v-bind:class='{ "is-active": show }')
      span
      span
      span
  .navbar-menu(:class='{ "is-active": show }')
    .navbar-end
      router-link.navbar-item(to='/torrents')
        | Torrents
        span.activity-count(v-show='getActiveCount > 0') {{ getActiveCount }}
      router-link.navbar-item(to='/settings')
        | Settings
      a.navbar-item(@click='logout')
        span Logout&nbsp;
        b-icon(size='is-small', icon='logout-variant')
</template>

<script>
// import
import { mapGetters } from 'vuex'
import auth from '@/authentication'
// export
export default {
  data() {
    return {
      show: false,
    }
  },
  computed: {
    ...mapGetters('torrents', ['getActiveCount']),
  },
  methods: {
    toggleShow() {
      this.show = !this.show
    },
    getLogoPath() {
      return process.env.NODE_ENV === 'production' ? require('../assets/logo.png') : require('../assets/logo_dev.png')
    },
    logout() {
      auth.logout()
    },
  },
}
</script>

<style lang="scss" scoped>
.logo {
  margin-right: 2.5rem;
}
.is-active {
  font-weight: 600;
}
.brand-link {
  background-color: unset;
  padding: 0;
}
.navbar-burger {
  background-color: #f9f9f9;
}
.navbar-item {
  gap: 5px;
}
.activity-count {
  $count-size: 16px;
  display: inline-block;
  background-color: black;
  opacity: 0.6;
  color: white;
  font-size: 13px;
  line-height: $count-size;
  width: $count-size;
  height: $count-size;
  border-radius: $count-size;
  text-align: center;
  z-index: 10;
  margin-left: 5px;
  @media only screen and (min-width: 1087px) {
    position: absolute;
    top: 8px;
    right: -1px;
  }
}
</style>
