<template>
  <div>
    <carousel-3d :autoplay="true" :autoplay-timeout="5000" :display="10" :width="200" :controls-visible="true">
      <slide v-for="(movie, i) in movies" :index="i" :key="i">
        <img :src="movie.image" :alt="movie.title" :class="`${movie.id}`" @click="goDetail($event)" />
      </slide>
    </carousel-3d>
  </div>
</template>

<script>
// import Carousel3d from 'vue-carousel-3d'
import router from '@/router'
import {Carousel3d, Slide} from 'vue-carousel-3d'
// import MoviePoster from './MoviePoster'
export default {
  name: 'MovieCarousel',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      slides: 10,
    }
  },
  components: {
    Carousel3d,
    Slide,
    // MoviePoster,
  },
  methods: {
    goDetail(event) {
      if (event.target.parentElement.className === 'carousel-3d-slide current'){
        router.push({
          name: 'movieDetail', 
          params: {
            id: event.target.className
          }
        })
      }
    }
  }
}
</script>

<style>

</style>