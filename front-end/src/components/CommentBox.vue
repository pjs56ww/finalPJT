<template>
  <div>
    <CommentList :comments="comments" />
  </div>
</template>

<script>
import CommentList from './CommentList'

export default {
  name: 'CommentBox',
  components: {
    CommentList,
  },
  props: {
    comments: {
      type: Array,
      required: true,
    }
  },
}
</script>

<style>

</style>