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

    <h2>How do I install a Custom CSS Scroll?</h2>

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
// @ is an alias to /src

export default {
  name: "Home",
  components: {}
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
