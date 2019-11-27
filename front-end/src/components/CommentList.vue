<template>
  <div>
    <div v-if="movie.comments.length">
      <div v-for="(comment, i) in movie.comments" :key="i">
        <p><star-rating :rating="comment.score/2"
          :read-only="true" :increment="0.5" :star-size="15"
          :show-rating="false" :inline="true"></star-rating>{{ comment.score }} {{ comment.content }}</p>
      </div>
    </div>
    <div v-else>없다. 코멘트</div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'CommentList',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  components: {
    StarRating
  },
  data() {
    return {
      comments: []
    }
  },
  methods: {
    getComments() {
      this.comments = this.movie.comments
    }
  },
  created() {
    this.getComments()
  }
}
</script>

<style>

</style>