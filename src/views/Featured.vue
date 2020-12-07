<template>
  <div class="home content">
    <!-- <h2><span class="icon"><i class="fas fa-palette"></i></span> Custom CSS</h2> -->
    <h2>🎨 Custom CSS</h2>
    <scroll-card
      :scrollData="scrolls['com.github.hannesfrank.remnote-css-rem-types']"
    />
    <h2>🍪 User Scripts</h2>
    <p>Coming Soon™</p>
  </div>
</template>

<script>
import ScrollCard from "../components/ScrollCard.vue";
import scrolls from "./../data.json";

export default {
  name: "Home",
  data: function() {
    return {
      scrolls: scrolls
    };
  },
  components: { ScrollCard }
};
</script>

<style>
.home {
  margin: 30px;
}
</style>
