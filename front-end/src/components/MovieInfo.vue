<template>
  <div>
    <h4 class="card-title">
      {{ movie.title }}
      <br />
      <span class="badge badge-info">{{ movie.score }}</span>
    </h4>
    <hr />
    <p class="card-text">{{ movie.genres }}</p>
    <p class="card-text">개봉: {{ movie.pubdate }}</p>
  </div>
</template>

<script>
export default {
  name: 'MovieInfo',
  props: {
    movie: {
      type: Object,
      required: true,
    }
  }
};
</script>

<style>
</style>