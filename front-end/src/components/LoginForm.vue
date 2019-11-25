<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>

    <div v-else class="login-form">

      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>

      <div class="form-group">
        <label for="id">ID</label>
        <input type="text" id="id" class="form-control" placeholder="ID" v-model="credentials.username">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" id="password" class="form-control" placeholder="Password" v-model="credentials.password">
      </div>
      <button class="btn btn-success" @click="login">Login</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

export default {
  name: 'LoginForm',
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      },
      loading: false,
      errors: [],
    }
  },
  methods: {
    login() {
      if (this.checkForm()) {
        this.loading = true
        // http://localhost:8000
        const SERVER_IP = process.env.VUE_APP_SERVER_IP

        axios.post(SERVER_IP + '/api-token-auth/', this.credentials)
          .then(response => {
            // 세션을 초기화, 사용하겠다.
            this.$session.start()
            // 응답 결과를 세션에 저장하겠다.
            this.$session.set('jwt', response.data.token)

            // vuex store 를 등록해서 $store로 접근 가능
            this.$store.dispatch('login', response.data.token)

            this.loading = false
            // vue router 를 통해 특정 페이지로 이동
            router.push('/')
          })
          .catch(error => {
            console.error(error)
            this.loading = false
          })
      }
    },
    checkForm() {
      this.errors = []
      if (!this.credentials.username) {
        this.errors.push('아이디를 입력해주세요.')
      }
      if (this.credentials.password.length < 8) {
        this.errors.push('비밀번호는 8글자 이상 입력해주세요.')
      }
      if (this.errors.length === 0) {
        return true
      } // else => undefined
    },
  }
}
</script>

<style>

</style>