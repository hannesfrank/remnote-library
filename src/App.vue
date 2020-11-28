<template>
  <header>
    <h1>RemNote Library</h1>
    <menu>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/library">Library</a></li>
        <li><a href="/package-guide">Package Guide</a></li>
      </ul>
    </menu>
  <div id="app">
    {VueComponent}
  </div>
</template>

<script>
import Home from './components/Home.vue';
import Library from './components/Library.vue';
import PackageGuide from './components/PackageGuide.vue';

const routes = {
  '/': Home,
  '/library': Library,
  '/package-guide': PackageGuide,
}

export default {
  name: "App",
  components: {
    Home,
    Library,
    PackageGuide
  },
  computed: {
    ViewComponent () {
      return routes[this.currentRoute] || 'not found';
    }
  }
};
</script>

<style>
:root {
  --width: 1200px;
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
}
</style>
