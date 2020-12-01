<template>
  <div id="library">
    <div class="search-bar">
      <Search v-model="query" />
      <div class="filter">
      </div>
    </div>
    <ScrollViewer :scrolls="filteredThemes" />
  </div>
</template>

<script>
import Search from "../components/Search.vue";
import ScrollViewer from "./../components/ScrollViewer.vue";
import scrolls from "./../data.json";

export default {
  components: {
    Search,
    ScrollViewer,
  },
  data() {
    return {
      publicPath: process.env.BASE_URL,
      scrolls: Object.values(scrolls),
      query: "",
    };
  },
  methods: {
    matchesQuery: function (query, theme) {
      const parts = query.split(" ");
      for (let part of parts) {
        if (!part) continue;
        part = part.toLowerCase();
        let foundPart = false;

        if (part.startsWith("#")) {
          const category = part.slice(1);
          for (const themeCategory of theme.categories) {
            foundPart ||= themeCategory.startsWith(category);
          }
        } else {
          console.log(theme.name, part);
          foundPart ||= theme.name.toLowerCase().includes(part);
        }
        if (!foundPart) {
          return false;
        }
      }
      return true;
    },
  },
  computed: {
    filteredThemes: function () {
      return this.scrolls.filter((theme) =>
        this.matchesQuery(this.query, theme)
      );
    },
    allCategories: function () {
      const all = new Set();
      for (const theme of this.scrolls) {
        for (const category of theme.categories) {
          all.add(category);
        }
      }
      return [...all];
    },
  },
};
</script>

<style>
.search-bar {
  border-bottom: 1px solid black;
}
</style>
