<template>
  <section id="app">
    <header>
      <div class="banner is-centered columns m-0">
        <div class="column is-one-quarter">
          <img src="./assets/library-logo.png" alt="" />
        </div>
        <div class="has-text-centered">
          <h1 class="title is-1 mt-4">
            <strong>Rem</strong>Note <em>Library</em>
          </h1>
          <h2 class="subtitle is-4">
            A package manager for RemNote.
          </h2>
        </div>
      </div>

      <!-- <div id="nav" class="is-size-1">
        <router-link to="/">Home</router-link> |
        <router-link to="/library">Library</router-link> |
        <router-link to="/scroll-guide">Scroll Guide</router-link>
        <router-link to="featured">Featured Scrolls</router-link>
        <router-link to="/about">About</router-link>
      </div> -->
      <!-- TODO: Edit color scheme and use is-primary or is-light here -->
      <nav class="navbar is-success">
        <div class="navbar-brand">
          <router-link exact-active-class="no-class-for-brand-image" class="navbar-item" to="/">
            <img
              src="./assets/library-logo.png"
              alt="RemNote Library: A Package Manager for RemNote."
            />
          </router-link>
          <div
            class="navbar-burger burger"
            aria-expanded="false"
            aria-label="menu"
            :class="{ 'is-active': burgerToggle }"
            @click="burgerToggle = !burgerToggle"
            data-target="navbarRemNoteLibrary"
          >
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>

        <div
          id="navbarRemNoteLibrary"
          class="navbar-menu"
          :class="{ 'is-active': burgerToggle }"
        >
          <div class="navbar-start">
            <router-link class="navbar-item" to="/">Home</router-link>
            <router-link class="navbar-item" to="/library">Library</router-link>
            <router-link class="navbar-item" to="/scroll-guide"
              >Publish a Scroll</router-link
            >
            <router-link class="navbar-item" to="/featured"
              >Featured Scrolls</router-link
            >
            <router-link class="navbar-item" to="/about">About</router-link>
          </div>
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="field is-grouped">
                <p class="control">
                  <!-- <a
                    class="bd-tw-button button"
                    data-social-network="Twitter"
                    data-social-action="tweet"
                    data-social-target="https://hannesfrank.github.io/remnote-library/#/"
                    target="_blank"
                    href="https://twitter.com/intent/tweet?text=RemNote Library: A package manager for RemNote.&amp;hashtags=remnote&amp;url=https://hannesfrank.github.io/remnote-library/&amp;via=jgthms"
                  >
                    <span class="icon">
                      <i class="fab fa-twitter"></i>
                    </span>
                    <span>
                      Tweet
                    </span>
                  </a> -->
                </p>
                <p class="control">
                  <a
                    class="button is-secondary"
                    href="https://github.com/hannesfrank/remnote-library"
                  >
                    <span class="icon">
                      <i class="fab fa-github"></i>
                    </span>
                    <span>GitHub</span>
                  </a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </nav>
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
  </section>
</template>
<script>
export default {
  data: function() {
    return {
      burgerToggle: false
    };
  }
};
</script>
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

  max-width: 1200px;
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

#nav a.router-link-exact-active {
  color: #42b983;
}

.navbar .navbar-item img {
  max-height: 2.5rem;
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
