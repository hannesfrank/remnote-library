<template>
  <div id="app">
    <header class="has-text-centered">
      <h1>
        <img class="logo" src="./assets/scroll.svg" alt="scroll icon" />
        <strong>Rem</strong>Note <em>Library</em>
      </h1>
      <div id="nav" class="is-size-1">
        <router-link to="/">Home</router-link> |
        <router-link to="/library">Library</router-link> |
        <router-link to="/scroll-guide">Scroll Guide</router-link>
      </div>
    </header>
    <div id="main">
      <router-view />
    </div>
    <footer class="p-2 has-text-centered">
      <div>Made with ❤ by Hannes Frank.</div>
      <div class="flaticons-attribution">
        Icons made by
        <a href="https://www.flaticon.com/authors/freepik" title="Freepik"
          >Freepik</a
        >
        from
        <a href="https://www.flaticon.com/" title="Flaticon"
          >www.flaticon.com</a
        >
      </div>
    </footer>
  </div>
</template>

<style>
:root {
  --background-color: blanchedalmond;
}
body {
  margin: 0;
  padding: 0;
  background-color: dimgray;
  margin: 0 auto;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  width: 1200px;
  min-height: 100vh;
  margin: 0px auto;
  background-color: var(--background-color);
  box-shadow: 0px 0px 10px 3px;
  display: flex;
  flex-direction: column;
}

header {
  width: 100%;
  background-color: tan;
  border-bottom: 1px solid black;
}

header img {
  display: inline-block;
  height: 128px;
  vertical-align: middle;
}

header h1 {
  font-size: 128px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#main {
  margin-bottom: 0;
  flex: 1 0 auto;
}

footer {
  width: 100%;
  background-color: tan;
  border-top: 1px solid black;
}

footer .flaticons-attribution {
  font-size: 12px;
}
footer .flaticons-attribution a {
  color: darkblue;
}
</style>
