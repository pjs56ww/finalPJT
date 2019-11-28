<template>
  <div id="app">
    <b-navbar toggleable="lg" variant="faded" type="light" id="nav" sticky>
      <b-navbar-brand v-if="isLoggedIn" href="/home">ㅇㅎㅊㅊ</b-navbar-brand>
      <b-navbar-brand v-else href="/">ㅇㅎㅊㅊ</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse v-if="isLoggedIn" id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item-dropdown dropright text="장르별">
            <b-dropdown-item v-for="option in genreSelect.options" 
                              :key="option.value"
                              @click="genreSelect.genreSelectedOption = option.value, byGenre = option.text"
                              @click.prevent="searchByGenre" href="/serch">
              {{ option.text }}
            </b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit.prevent="getMovies">
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchKeyword"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <span>{{ userName }}</span>
            </template>
            <b-dropdown-item href="#">회원정보</b-dropdown-item>
            <b-dropdown-item @click.prevent="logout" href="/logout">로그아웃</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
      <b-collapse v-else id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-item @click.prevent="login" href="/login">로그인</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div>
      <router-view :movies="movies" :byGenre="byGenre" :genreSelect="genreSelect" />
      <!-- <router-view /> -->
    </div>
  </div>
</template>

<script>
import router from "@/router";
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      searchKeyword: "",
      movies: [],
      byGenre: '',
      genreSelect: {
        genreSelectedOption: 0,
        options: [
          {
            value: "1",
            text: "드라마"
          },
          {
            value: "2",
            text: "스릴러"
          },
          {
            value: "3",
            text: "애니메이션"
          },
          {
            value: "4",
            text: "액션"
          },
          {
            value: "5",
            text: "가족"
          },
          {
            value: "6",
            text: "판타지"
          },
          {
            value: "7",
            text: "미스터리"
          },
          {
            value: "8",
            text: "코미디"
          },
          {
            value: "9",
            text: "범죄"
          },
          {
            value: "10",
            text: "어드벤쳐"
          },
          {
            value: "11",
            text: "SF"
          },
          {
            value: "12",
            text: "공연"
          },
          {
            value: "13",
            text: "멜로/로맨스"
          },
          {
            value: "14",
            text: "공포(호러)"
          },
          {
            value: "15",
            text: "뮤지컬"
          },
          {
            value: "16",
            text: "다큐멘터리"
          },
          {
            value: "17",
            text: "전쟁"
          },
          {
            value: "18",
            text: "기타"
          },
          {
            value: "19",
            text: "사극"
          }
        ]
      }
    };
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn;
    },
    userName() {
      return this.$store.getters.userName;
    }
  },
  // 최상위 App 컴퍼넌트가 렌더링 되면 실행하는 함수
  mounted() {
    setInterval(() => this.title = 'ㅇㅎㅊㅊ')
    if (this.$session.has("jwt")) {
      const token = this.$session.get("jwt");
      this.$store.dispatch("login", token);
    }
  },
  methods: {
    login() {
      router.push("/login")
    },
    logout() {
      this.$session.destroy();
      this.$store.dispatch("logout");
      router.push("/");
      localStorage.removeItem('token')
    },
    getMovies() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/search/`, {
          params: {
            keyword: this.searchKeyword
          }
        })
        .then(response => {
          this.byGenre = ''
          this.movies = response.data;
          router.push("/search").catch(err => err)
          this.searchKeyword = ''
        })
        .catch(error => {
          console.error(error);
        });
    },
    searchByGenre() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios
        .get(`${SERVER_IP}/api/v1/genredb/${this.genreSelect.genreSelectedOption}`)
        .then(response => {
          this.movies = response.data.movies
          router.push("/search").catch(err => err)
        })
        .catch(error => {
          console.error(error)
        })
    },
    
  }
  // data 에 변화가 일어나는 시점에 실행하는 함수
  // updated() {
  //   this.isLoggedIn = this.$session.has('jwt')
  // },
};
</script>

<style>
body {
  font-family: 'Raleway', sans-serif;
}
</style>
