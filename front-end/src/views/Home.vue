<template>
  <div class="home">
    <HomeImage :movies="movies" />
    <MovieCarousel :movies="movies" />
    <!-- <carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="5" :width="200">
      <slide v-for="(movie, i) in movies" :index="i" :key="i">
        <img :src="movie.image" alt="">
      </slide>
    </carousel-3d> -->
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import MovieCarousel from '@/components/MovieCarousel'
import HomeImage from '@/components/HomeImage'
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해서 보여주는 library
import { mapGetters } from 'vuex'
// import { Carousel3d, Slide } from 'vue-carousel-3d'

export default {
  name: 'Home',
  components: {
    // 'carousel-3d': Carousel3d.Carousel3d,
    // 'slide': Carousel3d.Slide,
    MovieCarousel,
    HomeImage,
  },
  data() {
    return {
      movies: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
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
        console.log(this.isLoggedIn)
        router.push('/login')
      }
    },
    getMovie() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/home/`)
        .then(response => {
          // console.log(response)
          this.movies = response.data
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    // this.checkLoggedIn()
    if (this.isLoggedIn) {
      this.getMovie()
    }
  },
  watch: {
    isLoggedIn() {
      this.checkLoggedIn()
      this.getMovie()
    },
  }
}
</script>

<style>

</style>