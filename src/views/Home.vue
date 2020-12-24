<template>
  <div class="home content">
    <h2>What is this?</h2>
    <figure class="image is-128x128 is-pulled-right my-0">
      <img src="../assets/scroll.svg" />
    </figure>
    <p>
      This is my attempt to make sharing customizations for RemNote easier.
      Those customizations are packaged into
      <em
        ><img src="../assets/scroll.svg" alt="scroll icon" class="icon" />
        Scrolls</em
      >.
    </p>
    <p>
      At the moment you can only find Custom CSS Scrolls here (themes and
      widgets). For more information about Custom CSS look at this forum post:
      <a
        href="https://forum.remnote.io/t/what-is-custom-css-and-how-do-i-use-it/1231"
        >See: What is Custom CSS and how do I use it?</a
      >.
    </p>
    <p>
      See <router-link to="/about">About</router-link> for more information
      about the library:
    </p>
    <ul>
      <li>
        <router-link to="/about#roadmap">Roadmap</router-link>
      </li>
      <li>
        <router-link to="/about#vision">Vision</router-link>
      </li>
    </ul>
    <h2>What can I get here?</h2>
    <div class="is-flex is-flex-wrap-wrap">
      <scroll-card
        :scrollData="scrolls['com.github.hannesfrank.remnote-css-rem-types']"
        class="m-2"
      />
      <scroll-card
        :scrollData="
          scrolls['com.github.hannesfrank.remnote-library.kanban-board']
        "
        class="m-2"
      />
    </div>
    See <router-link to="featured">Featured Scrolls</router-link> or the
    <router-link to="library">Library</router-link> for all available
    <em
      ><img src="../assets/scroll.svg" alt="scroll icon" class="icon" />
      Scrolls</em
    >.

    <h2 id="custom-css-install-guide">How do I install a Custom CSS Scroll?</h2>

    <figure class="image is-16by9">
      <iframe
        class="has-ratio"
        width="560"
        height="315"
        src="https://www.youtube.com/embed/4Y5MeO3g5Ik"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </figure>

    <ol>
      <li>
        Find the
        <em>
          <img src="../assets/scroll.svg" alt="scroll icon" class="icon" />
          Scroll
        </em>
        you want to install, click to open it and scroll to
        <em>Installation</em>.
      </li>
      <li>Click the <em>Custom CSS Block</em> button.</li>
      <li>
        Go to RemNote and open the Custom CSS page using
        <kbd>Ctrl</kbd>+<kbd>P</kbd>.
      </li>
      <li>
        Paste the <em>Custom CSS Block</em> with
        <kbd>Ctrl</kbd>+<kbd>V</kbd>.
      </li>
    </ol>

    <article class="message is-info">
      <div class="message-header">
        <p>Don't worry!</p>
      </div>
      <div class="message-body">
        The install process will not always be that complicated.
        <br />
        Once the API is extended it will be just a button click to install,
        update or remove!
      </div>
    </article>
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

img.icon {
  display: inline-block;
  width: 1em;
  height: 1em;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
  line-height: 1;
  position: relative;
  top: -0.05em;
  vertical-align: middle;
}
</style>
