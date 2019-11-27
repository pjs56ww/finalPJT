<template>
  <img :src="movie.image" alt="" />
</template>

<script>
export default {
  name: 'MoviePoster',
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
}
</script>

<style>

</style>