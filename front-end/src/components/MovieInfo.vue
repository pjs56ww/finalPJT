<template>
  <div>
    <h4 class="card-title">
      {{ movie.title }}
      <br />
      <span class="badge badge-info">{{ movie.score }}</span>
    </h4>
    <hr />
    <p class="card-text">{{ movieGenre.join(', ') }}</p>
    <p class="card-text">개봉: {{ movie.openDt }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  props: {
    movie: {
      type: Object,
      required: true,
    },
    genres: {
      type: Array,
    }
  },
  data() {
    return {
      movieGenre: []
    }
  },
  created() {
    for (const genre of this.movie.genres) {
      this.movieGenre.push(this.genres[genre - 1].text)
    }
  }
};
</script>

<style>
</style>