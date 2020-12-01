<template>
  <div class="scroll-viewer">
    <ScrollCard
      v-for="theme in scrolls"
      v-bind:key="theme.name"
      v-bind:title="theme.name"
      v-bind:stars="theme.stars"
      v-bind:installed="theme.installed"
      v-bind:categories="theme.categories"
      v-bind:thumb="theme.thumb"
    />
  </div>
</template>

<script>
import ScrollCard from "./ScrollCard.vue";

export default {
  components: {
    ScrollCard,
  },
  props: ["scrolls"],
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
};
</script>

<style scoped>
.scroll-viewer {
  margin: 0 auto;
  padding: 10px 10px;
  width: 100%;

  display: flex;
  flex-flow: row wrap;
  align-content: flex-start;
  justify-content: center;
}

.scroll-viewer .card {
  margin: 10px;
}
</style>
