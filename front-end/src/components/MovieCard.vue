<template>
  <div class="movieCard">
    <img :src="movie.image" alt="" :width="200">
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
  },
  data() {
    return {
    }
  },
}
</script>

<style>

</style>