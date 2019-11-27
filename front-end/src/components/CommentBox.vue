<template>
  <div>
    <CommentList :movie="movie" />
    <comment-modal :movie="movie"/>
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
}
</script>

<style>

</style>