<template>
  <img :src="movie.image" :alt="movie.title" />
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