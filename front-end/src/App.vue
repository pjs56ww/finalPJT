<template>
  <div id="app">
    <!-- <div id="nav">
      <div v-if="isLoggedIn">
        <router-link to="/home">Home</router-link> |
        <a @click.prevent="logout" href="/logout">Logout</a>
      </div>
      <div v-else>
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">Signup</router-link>
      </div>
    </div>-->
    <div class="">
      <b-navbar toggleable="lg" type="light" id="nav" sticky>
        <b-navbar-brand href="/home">ㅇㅎㅊㅊ</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse v-if="isLoggedIn" id="nav-collapse" is-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form @submit.prevent="getMovies">
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchKeyword"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <span>User</span>
              </template>
              <b-dropdown-item href="#">회원정보</b-dropdown-item>
              <b-dropdown-item @click.prevent="logout" href="/logout">로그아웃</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
        <b-collapse v-else id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <router-link to="/login">Login</router-link>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <div>
      <router-view :movies="movies"/>
    </div>
  </div>
</template>

<script>
import router from "@/router";
import axios from "axios"

export default {
  name: "App",
  // data() {
  //   return {
  //     isLoggedIn: this.$session.has('jwt')
  //   }
  // },
  data() {
    return {
      searchKeyword: '',
      movies: [],
    }
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    }
  },
  // 최상위 App 컴퍼넌트가 렌더링 되면 실행하는 함수
  mounted() {
    if (this.$session.has("jwt")) {
      const token = this.$session.get("jwt");
      this.$store.dispatch("login", token);
    }
  },
  methods: {
    logout() {
      this.$session.destroy();
      this.$store.dispatch("logout");
      router.push("/login");
    },
    getMovies() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/search/`, {
        params: {
          keyword: this.searchKeyword
        }
      })
        .then(response => {
          this.movies = response.data
          router.push("/search").catch(err => err)
          this.searchKeyword = ''
        })
        .catch(error => {
          console.error(error)
        })
    }
  }
  // data 에 변화가 일어나는 시점에 실행하는 함수
  // updated() {
  //   this.isLoggedIn = this.$session.has('jwt')
  // },
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
