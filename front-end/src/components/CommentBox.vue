<template>
  <div>
    <CommentList :movie="movie" />
    <b-button v-b-modal.cModal>평점 작성하기</b-button>
    <comment-modal id="cModal" :movie="movie" @createComment="createComment"/>
  </div>
</template>

<script>
import CommentList from './CommentList'
import CommentModal from './CommentModal'

export default {
  name: 'CommentBox',
  components: {
    CommentList,
    CommentModal,
  },
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    createComment(data) {
      this.$emit('createComment', data)
    }
  }
}
</script>

<style>

</style>