<template>
  <img :src="movie.image" :alt="movie.title" @click.prevent="goDetail" href="/movie" />
</template>

<script>
import router from '@/router'

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
  methods: {
    goDetail() {
      router.push({
        name: 'movieDetail', 
        params: {
          id: this.movie.id
        }
      })
    }
  }
}
</script>

<style>

</style>