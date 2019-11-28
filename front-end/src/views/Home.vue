<template>
  <div class="home">
    <div style=" text-align: center;">
      <b-img-lazy :src="bgImage" alt="" fluid style="width:1000px; height: auto;"></b-img-lazy>
    </div>
    <MovieCarousel :movies="movies" />
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import MovieCarousel from '@/components/MovieCarousel'
// import HomeImage from '@/components/HomeImage'
// import jwtDecode from 'jwt-decode' // JWT 의 payload 값을 해석해서 보여주는 library
import { mapGetters } from 'vuex'
// import { Carousel3d, Slide } from 'vue-carousel-3d'


export default {
  name: 'Home',
  components: {
    // 'carousel-3d': Carousel3d.Carousel3d,
    // 'slide': Carousel3d.Slide,
    MovieCarousel,
    // HomeImage,
  },
  data() {
    return {
      allMovies: [],
      movies: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      bgImage: ''
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
      if (!this.isLoggedIn) {
        router.push('/')
      }
    },
    getMovie() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/home/`)
        .then(response => {
          this.movies = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
    getBgImg() {
      const getRandomInt = function(min, max) {
        min = Math.ceil(min)
        max = Math.floor(max)
        return Math.floor(Math.random() * (max - min)) + min
      }
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/search/`, {
          params: {
            keyword: ''
          }
        })
        .then(response => {
          this.allMovies = response.data
          const randNum = getRandomInt(0, this.allMovies.length)
          this.bgImage = this.allMovies[randNum].backgroundImage
        })
        .catch(error => {
          console.error(error);
        })
      
    }
  },
  created() {
    this.getBgImg()
  },
  // Vue 가 화면에 그려지면 실행하는 함수
  mounted() {
    this.checkLoggedIn()
    this.getMovie()
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