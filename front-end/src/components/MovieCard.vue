<template>
  <div class="movieCard">
    <img :src="movie.image" alt="">
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>

</style>