<template>
  <a @click.prevent="goDetail" href="/movie" style=" text-align: center;">
    <MoviePoster :movie="movie" :width="200" :height="300"/>
  </a>
  <!-- <img :src="movie.image" :alt="movie.title" @click.prevent="goDetail" href="/movie" /> -->
</template>

<script>
import MoviePoster from './MoviePoster'
import router from '@/router'

export default {
  name: 'MovieCard',
  components: {
    MoviePoster,
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
    }
  },
  methods: {
    goDetail() {
      router.push({
        name: 'movieDetail', 
        params: {
          id: this.movie.id
        }
      })
    }
  }
}
</script>

<style>
  .card-title {
    height: 65px;
  }
  .card-text {
    height: 40px;
  }
</style>