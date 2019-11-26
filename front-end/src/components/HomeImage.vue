<template>
  <div class="homeImage">
    <img :src="backImg" alt="" width="200">
  </div>
</template>

<script>
const getRandomInt = function(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min)) + min
}
export default {
  name: 'HomeImage',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      backImg: this.movies[getRandomInt(0, 10)].image,
    }
  },
  updated: {
  }
}
</script>

<style>

</style>