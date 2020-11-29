<template>
  <div id="library">
    <div class="search-bar">
      <Search v-model="query" />
      <div class="filter">
      </div>
    </div>
    <PackageViewer :themes="filteredThemes" />
  </div>
</template>

<script>
import Search from "../components/Search.vue";
import PackageViewer from "./../components/PackageViewer.vue";
import themes from "./../data.json";

export default {
  components: {
    Search,
    PackageViewer,
  },
  data() {
    return {
      publicPath: process.env.BASE_URL,
      themes: Object.values(themes),
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
      return this.themes.filter((theme) =>
        this.matchesQuery(this.query, theme)
      );
    },
    allCategories: function () {
      const all = new Set();
      for (const theme of this.themes) {
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
  background-color: rgb(34, 39, 68);
}
</style>
