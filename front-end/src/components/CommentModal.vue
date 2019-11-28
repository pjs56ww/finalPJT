<template>
  <b-modal id="cModal" title="평점작성하기" 
    @ok="createComment"
    @show="resetModal"
    @hidden="resetModal"
  >
    <form ref="form" @submit="createComment">
      <b-form-group>
        <div class="mb-3">
        <star-rating :rating="0.5" :show-rating="false" :increment="0.5"
          :star-size="20" @rating-selected="setRating" :inline="true"></star-rating>
        <span>{{ score }} 점!</span>
        </div>
        <b-form-input
          id="comment-input"
          v-model="content"
          required
        ></b-form-input>
      </b-form-group>
    </form>
    <!-- <form @submit.prevent="createComment">
      <star-rating :rating="0.5" :show-rating="false" :increment="0.5"
      :star-size="20" @rating-selected="setRating" :inline="true"></star-rating>
      <span>{{ score }} 점!</span>
      <input type="text" class="form-control" v-model="content" />
      <b-button variant="outline-primary" type="submit">작성하기</b-button>
    </form> -->
  </b-modal>
</template>

<script>
import StarRating from 'vue-star-rating'
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
      const data = {content: this.content, score: this.score}
      this.$emit('createComment', data)
    },
    resetModal() {
      this.content = '',
      this.score = 1
    }
  }
}
</script>

<style>

</style>