<template>
  <div class="movieCarousel">
    <carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="7" :width="200">
      <slide v-for="(movie, i) in movies" :index="i" :key="i">
        <MovieCard :movie="movie" />
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
// import Carousel3d from 'vue-carousel-3d'
import {Carousel3d, Slide} from 'vue-carousel-3d'
import MovieCard from './MovieCard'
export default {
  name: 'MovieCarousel',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  components: {
    Carousel3d,
    Slide,
    MovieCard,
  }
}
</script>

<style>

</style>