<template>
  <div class="homeImage">
    <img :src="movies[0].backgroundImage" alt="" :width="windowWidth">
  </div>
</template>

<script>
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
      windowWidth: window.innerWidth
    }
  },
  updated: {
    windowWidth() {
      this.windowWidth = window.innerWidth
    }
  }
}
</script>

<style>

</style>