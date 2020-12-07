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

    <h2 id="custom-css-install-guide">How do I install a Custom CSS Scroll?</h2>

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
      <li>Click the first copy button <em>Custom CSS Template</em>.</li>
      <li>
        Go to RemNote and open the Custom CSS page using
        <kbd>Ctrl</kbd>+<kbd>P</kbd>.
      </li>
      <li>
        Paste the <em>Custom CSS Template</em> with
        <kbd>Ctrl</kbd>+<kbd>V</kbd>.
      </li>
      <li>Click the second copy button <em>CSS Code Block</em>.</li>
      <li>
        Under the <strong>Code</strong> heading create a checked todo item and
        insert a code block.
      </li>
      <ul>
        <li>Make sure the language is set to <em>CSS</em>.</li>
      </ul>
      <li>Paste <em>CSS Code Block</em> into the code block.</li>
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

kbd {
  background-color: #eee;
  border-radius: 3px;
  border: 1px solid #b4b4b4;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.2),
    0 2px 0 0 rgba(255, 255, 255, 0.7) inset;
  color: #333;
  display: inline-block;
  font-size: 0.85em;
  font-weight: 700;
  line-height: 1;
  padding: 2px 4px;
  white-space: nowrap;
}
</style>
