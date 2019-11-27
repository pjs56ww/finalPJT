<template>
  <b-container fluid class="p-4 bg-dark">
    <b-img :src="movie.backgroundImage" fluid-grow alt="" />
    <b-img thumbnail :src="movie.image" fluid :width="200" />
    <CommentBox :movie="movie" />
  </b-container>
</template>

<script>
import axios from "axios"
import { mapGetters } from 'vuex'
import CommentBox from '@/components/CommentBox'
// import MoviePoster from "./MoviePoster"

export default {
  name: "MovieDetail",
  props: {},
  components: {
    CommentBox,
    // MoviePoster,
  },
  data() {
    return {
      movie: {}
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  // created() {
    
  // },
  created() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    const headers = this.options.headers
    axios.get(`${SERVER_IP}/api/v1/movies/${this.$route.params.id}/`, {headers: headers})
      .then(response => {
        this.movie = response.data
      })
      .catch(error => {
        console.error(error)
      })
  }
}
</script>

<style>
</style>