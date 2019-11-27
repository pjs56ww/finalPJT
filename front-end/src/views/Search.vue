<template>
  <div>
    <div v-if="movies.length">
      <MovieList :movies="movies" class="container mx-auto" />
    </div>
    <div v-else>
      <p>검색결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'
export default {
  name: 'Search',
  components: {
    MovieList,
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