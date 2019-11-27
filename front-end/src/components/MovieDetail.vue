<template>
  <div class="movieDetail">
    
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "MovieDetail",
  props: {},
  data() {
    return {
      movie: {}
    }
  },
  created() {
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    axios.get(`${SERVER_IP}/api/v1/movies/${this.$route.params.id}/`, {headers: this.$store.getters.options.headers})
     .then(response => {
       this.movie = response.data
     })
     .catch(error => error)
  }
}
</script>

<style>
</style>