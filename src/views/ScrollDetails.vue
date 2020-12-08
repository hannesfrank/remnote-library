<template>
  <div class="scroll-details-page content">
    <div class="content">
      <div class="shelf-icon icon is-large is-pulled-left mr-2">
        <i class="fas fa-palette fa-2x" aria-hidden="true"></i>
      </div>
      <p class="title is-4">
        {{ name }}
      </p>
      <p class="subtitle is-size-7">
        {{ id }}
      </p>
    </div>

    <ScrollDetails :scrollData="scrollData" />
  </div>
</template>
<script>
import ScrollDetails from "../components/ScrollDetails.vue";

export default {
  components: {
    ScrollDetails
  },
  props: ["scrollData"],
  data() {
    return {
      publicPath: process.env.BASE_URL,
      showDetails: false
    };
  },
  methods: {},
  computed: {
    // Polymorphy: There could be cards for different kinds of scrolls.
    // Each type having its own attributes.
    // TODO: consider extracting the scrollData in an init method and not make so many computed properties
    id: function() {
      return this.scrollData.id;
    },
    name: function() {
      return this.scrollData.name;
    }
  }
};
</script>

<style lang="scss">
/* Fix bug in bulma where there is a missing gap */
.scroll-details-page {
  margin: 30px;
}
</style>
