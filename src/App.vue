<template>
  <div id="app">
    <Search v-model="query" />
    <Library :themes="filteredThemes" />
  </div>
</template>

<script>
import Search from "./components/Search.vue";
import Library from "./components/Library.vue";
import themes from "./data.json";

export default {
  name: "App",
  components: {
    Search,
    Library,
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
      console.log(theme.name, "XXXXX");
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
:root {
  --width: 750px;
}
html {
  overflow-y: hidden !important;
}
body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: lightgray;
  color: #2c3e50;
  margin: 0px;
  width: var(--width);
  height: 500px;
}
</style>
