<template>
  <div class="home">
    <nav class="navbar navbar-expand-lg navbar-light bg-light sticky-top">
      <a href="#">JSPark's Movie</a>
    </nav>

  </div>
</template>

<script>
// import axios from 'axios'
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해서 보여주는 library
import { mapGetters } from 'vuex'
import router from '@/router'

export default {
  name: 'Home',
  components: {

  },
  data() {
    return {
      todos: [],
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인 되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {
      // // 1. 세션을 시작해서 
      // this.$session.start()

      // // 2. 'jwt' 가 있는지 확인하겠다.
      // if (!this.$session.has('jwt')) {
      //   // 없다면 로그인 페이지로 보내겠다.
      //   router.push('/login')
      // }
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
  },
  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    // this.checkLoggedIn()
    if (this.isLoggedIn) {
      console.log(this.isLoggedIn)
    }
  },
  watch: {
    isLoggedIn() {
      this.checkLoggedIn()
    },
  }
}
</script>

<style>

</style>