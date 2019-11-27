<template>
  <div>
    <b-img :src="bgImage" alt="" fluid />
  </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'
// import WelcomeImage from '@/components/WelcomeImage.vue'

import { mapGetters } from 'vuex'

export default {
  name: 'Welcome',
  components: {
    // WelcomeImage,
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
      bgImage:''
    }
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인 되어있을 시 (/home)으로 보내겠다.
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
    },    
    checkLoggedIn() {
      if (this.isLoggedIn) {
        router.push('/home')
      }
    },
    
  },
  mounted() {
    this.checkLoggedIn()
    this.getBgImg()
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