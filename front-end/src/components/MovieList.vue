<template>
  <div class="row">
    <div class="col-lg-3 col-md-4 col-sm-6 col-12 py-2 px-1" v-for="movie in movies" :key="movie.movieCd">
      <div class="card">
        <MovieCard :movie="movie" class="card-img-top" :width="200" :height="350" />
        <movie-info :movie="movie" :genres="genres" class="card-body" />
      </div>
    </div>
  </div>
</template>

<script>
import MovieCard from './MovieCard'
import MovieInfo from './MovieInfo'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
    MovieInfo,
  },
  props: {
    movies: {
      type: Array,
      required: true,
    },
    genres: {
      type: Array,
    }
  }
}
</script>

<style>

</style>