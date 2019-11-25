<template>
  <div id="app">
    <div id="nav">
      <div v-if="isLoggedIn">
        <router-link to="/">Home</router-link> |
        <a @click.prevent="logout" href="/logout">Logout</a>
        <!-- prevent 를 사용하는 이유는 href 로 redirect 를 방지하기 위함 -->
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link>
      </div>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import router from '@/router'

export default {
  name: 'App',
  // data() {
  //   return {
  //     isLoggedIn: this.$session.has('jwt')
  //   }
  // },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  // 최상위 App 컴퍼넌트가 렌더링 되면 실행하는 함수
  mounted() {
    if (this.$session.has('jwt')) {
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  },
  methods: {
    logout() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('/login')
    }
  },
  // data 에 변화가 일어나는 시점에 실행하는 함수
  // updated() {
  //   this.isLoggedIn = this.$session.has('jwt')
  // },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
