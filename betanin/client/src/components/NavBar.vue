<template lang="pug">
  nav.navbar
    .navbar-brand
      router-link.navbar-item(to='/')
        img#logo(
          :src='getLogoPath()'
          height='100%'
        )
      a.navbar-burger(
        role='button',
        @click='toggleShow',
        v-bind:class="{ 'is-active' : show }"
      )
        span
        span
        span
    .navbar-menu(:class="{ 'is-active': show }")
      .navbar-end
        router-link.navbar-item(to='/torrents/active')
          | Activity
          span#activity-count(v-show='getActivityCount > 0') {{ getActivityCount }}
        router-link.navbar-item(to='/torrents/complete') History
        router-link.navbar-item(to='/settings') Settings
</template>

<script>
// import
import { mapGetters } from 'vuex'
// export
export default {
  data () {
    return {
      show: false
    }
  },
  computed: {
    ...mapGetters('torrents', [
      'getActivityCount'
    ])
  },
  methods: {
    toggleShow () {
      this.show = !this.show
    },
    getLogoPath () {
      // eslint-disable-next-line
      return __NODE_ENV__ === 'production'
        ? require('../assets/logo.png')
        : require('../assets/logo_dev.png')
    }
  }
}
</script>

<style lang='scss' scoped>
  #logo {
     margin-right: 2.5rem;
  }
  .is-active {
    font-weight: 600;
  }
  #activity-count {
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
