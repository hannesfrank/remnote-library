<template>
  <div class="scroll-viewer">
    <ScrollCard
      v-for="scroll in scrolls"
      :key="scroll.id"
      :scrollData="scroll"
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

.scroll-viewer .scroll-card {
  margin: 10px;
}
</style>
