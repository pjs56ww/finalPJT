<template>
  <div>
    <form @submit.prevent="createComment">
      <star-rating :rating="0.5" :show-rating="false" :increment="0.5"
      :star-size="20" @rating-selected="setRating"></star-rating>
      <span>{{ score }} 점!</span>
      <input type="text" class="form-control" v-model="content" />
      <b-button variant="outline-primary" type="submit">작성하기</b-button>
    </form>

    <hr />
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'CommentModal',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  components: {
    StarRating,
  },
  data() {
    return {
      score: 1,
      content: '',
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  methods: {
    setRating(rating) {
      this.score = 2 * rating
    },
    createComment() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const headers = this.options
      const data = {content: this.content, score: this.score}
      axios.post(`${SERVER_IP}/api/v1/movies/${this.movie.id}/comment/`, data, headers)
       .then(() => {
         this.content = ''
         this.score = 1
         alert('작성되었습니다.')
       })
       .catch(error => {
         console.error(error)
       })
    }
  }
}
</script>

<style>

</style>