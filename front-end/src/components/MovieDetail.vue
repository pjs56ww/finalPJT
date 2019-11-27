<template>
  <b-container fluid class="p-4 bg-dark">
    <b-img :src="movie.backgroundImage" fluid-grow alt="" />
    <b-img thumbnail :src="movie.image" fluid :width="200" />
    <span>{{ movie.comments }}</span>
    <!-- <CommentBox :comments="movie.comments" /> -->
  </b-container>
</template>

<script>
import axios from "axios"
import { mapGetters } from 'vuex'
// import CommentBox from './CommentBox'
// import MoviePoster from "./MoviePoster"

export default {
  name: "MovieDetail",
  props: {},
  components: {
    // CommentBox,
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
  created() {
    
  },
  mounted() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    axios.get(`${SERVER_IP}/api/v1/movies/${this.$route.params.id}/`, {headers: this.options.headers})
     .then(response => {
       this.movie = response.data
     })
     .catch(error => error)
  }
}
</script>

<style>
</style>