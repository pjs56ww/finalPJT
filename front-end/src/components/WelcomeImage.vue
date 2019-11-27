<template>
  <div class="mx-auto">
    <img :src="bgImage" alt="" class="mx-auto">
  </div>
</template>

<script>
export default {
  name: 'WelcomeImage',
  props: {
    bgImage: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
    }
  },
  updated: {
  }
}
</script>

<style>

</style>