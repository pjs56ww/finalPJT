<template>
  <div class="home">
    <HomeImage :bgImage="bgImage" />
    <MovieCarousel :movies="movies" />
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

const getRandomInt = function(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min
}

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
          this.bgImage = this.movies[getRandomInt(0, 10)].backgroundImage
        })
        .catch(error => {
          console.error(error)
        })
    }
  },
  // Vue 가 화면에 그려지면 실행하는 함수
  mounted: function () {
    this.$nextTick(function () {
      this.getMovie()
    })
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