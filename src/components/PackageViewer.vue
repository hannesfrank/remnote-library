<template>
  <div class="package-viewer">
    <PackageCard
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
import PackageCard from "./PackageCard.vue";

export default {
  components: {
    PackageCard,
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
.package-viewer {

  margin: 0 auto;
  padding: 10px 10px;
  width: 100%;
  height: 100%;
  background-color: white;

  display: flex;
  flex-flow: row wrap;
  overflow-y: scroll;
  align-content: flex-start;
}

.package-viewer .card {
  margin: 5px;
}
</style>
