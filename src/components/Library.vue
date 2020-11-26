<template>
  <div class="library">
    <Card
      v-for="theme in themes"
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
import Card from "./Card.vue";

export default {
  name: "Library",
  components: {
    Card,
  },
  props: ["themes"],
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
};
</script>

<style scoped>
.library {
  margin: 0;
  padding: 10px 10px;
  width: 100%;
  height: 100%;
  background-color: white;
  display: flex;
  flex-flow: row wrap;
  overflow-y: scroll;
  justify-content: space-between;
  align-content: flex-start;
}
.filler {
  flex-grow: 1;
}
</style>
