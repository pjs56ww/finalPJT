<template>
  <div>
    <div v-if="movies.length">
      <div v-for="movie in movies" :key="movie.movieCd">
        <MovieCard :movie="movie" />
      </div>
    </div>
    <div v-else>
      <p>검색결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard'
export default {
  name: 'Search',
  components: {
    MovieCard,
  },
  props: {
    movies: {
      type: Array
    }
  }
}
</script>

<style>

</style>