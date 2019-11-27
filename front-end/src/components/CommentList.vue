<template>
  <div>
    <div v-if="comments.length">있다. 코멘트</div>
    <div v-else>없다. 코멘트</div>
  </div>
</template>

<script>
export default {
  name: 'CommentList',
  props: {
    comments: {
      type: Array,
    }
  },
  components: {

  }
}
</script>

<style>

</style>