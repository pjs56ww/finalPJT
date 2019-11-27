<template>
  <div>
    <WelcomeImage :bgImage="bgImage" />
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
import WelcomeImage from '@/components/WelcomeImage.vue'

import { mapGetters } from 'vuex'
const getRandomInt = function(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min
}
export default {
  name: 'Welcome',
  components: {
    WelcomeImage,
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ]),
    
    
  },
  data() {
    return {
      movies: [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}],
      bgImage:''
    }
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인 되어있을 시 (/home)으로 보내겠다.
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
    },
    putBackground() {
      return this.movies[getRandomInt(0, 10)].backgroundImage 
    },
    
    checkLoggedIn() {
      if (this.isLoggedIn) {
        console.log(this.isLoggedIn)
        router.push('/home')
      }
    },
    
  },
  created() {
    this.$nextTick(function () {
      this.getMovie()
    })
    this.bgImage = this.putBackground()
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