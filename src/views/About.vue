<template>
  <div class="about content">
    <h2>F.A.Q. and Tips</h2>
    <p>
      Ask something on the <a href="https://bit.ly/REMNOTEdiscord">Discord</a>,
      the <a href="https://forum.remnote.io">Forum</a> or
      <a href="https://github.com/hannesfrank/remnote-library">Github</a>.
    </p>
    <h3>
      Where can I report problems or make a suggestion for a (Custom CSS)
      Scroll?
    </h3>
    <p>
      There is a Report link in the metadata section of the Custom CSS Template
      Block which can be used to quickly create an issue.
    </p>
    <p>
      Otherwise go to the Homepage of the Scroll and report the issue there.
    </p>
    <h3 id="tag-prefix">
      It is hard to select the correct styling tag or list all styling tags.
    </h3>
    <figure class="image is-pulled-right mt-0">
      <img
        src="../assets/tip-prefix-tags.png"
        style="width: 175px"
        alt="Tip prefix tags"
      />
    </figure>
    <p>
      If you have trouble (comfortably) selecting the correct styling tag using
      the <kbd>Ctrl</kbd> + <kbd>P</kbd> search box other rem are also shown
      consider giving your styling tags a prefix similar to Universal
      Descriptors.
    </p>
    <p>
      You can use any special characters (like <code>_ ! § $ % &amp; /</code>)
      as they are ignored by the code.
    </p>
    <p>
      Another option is to copy the tag <kbd>Ctrl</kbd> + <kbd>Alt</kbd> +
      <kbd>S</kbd> and paste it with a shortcut or trigger sequence using a
      third-party tool like Autohotkey or Keyboard Maestro.
    </p>

    <h2>Contributing</h2>
    <p>
      You can <router-link to="/scroll-guide">share Scrolls</router-link> or
      help developing the library itself.
    </p>

    <h2 id="roadmap">WIP: roadmap</h2>
    <h3>
      Features for the library
    </h3>
    <ul>
      <li>Link scrolls for user scripts</li>
      <li>List installed scrolls</li>
    </ul>
    <h3>Scrolls</h3>
    <ul>
      <li>Divider</li>
      <li>Kanban Board</li>
      <li>Table</li>
      <li>Sidebar Icons</li>
      <li>Line Numbered Code Blocks</li>
    </ul>

    <h2 id="vision">WIP: Vision and Theme</h2>
    <p>A library is a institution to share the knowledge of humankind.</p>
    <p>
      Knowledge of all kinds - facts, procedures and even computer code - have
      the unique property that it can be shared without additional properties
      without additional cost. This is magical.
    </p>

    <p>
      This library hosts numerous scroll which aid you on your learning journey.
      Take a break from watering your tree of knowledge and wander through the
      halls of this place.
    </p>
    <p>
      Later all kinds of
      <em
        ><img src="../assets/scroll.svg" alt="scroll icon" class="icon" />
        Scrolls</em
      >
      could be supported:
    </p>
    <ul>
      <li>🍪 User Scripts</li>
      <li>Links resources like Video and Text Tutorials</li>
      <li>
        Even plugins and shared documents (but those are also listed in RemNote
        itself).
      </li>
    </ul>
    Those will be organized into 📚 <em>Shelves</em>.

    <h2>Special Thanks</h2>
    <ul>
      <li>
        <a href="https://github.com/WildGenius">WildGenius</a> and others for
        extensive feedback.
      </li>
    </ul>
    <h2>Support</h2>
    <p>
      Yes, please 🙃
    </p>
    <h2>Changelog</h2>
    <h3>2020-12-09</h3>
    <ul>
      <li>
        Feature: Custom CSS Metadata blocks now have a report link to quickly
        create an issue.
      </li>
    </ul>
    <h3>2020-12-08</h3>
    <ul>
      <li>Feature: Each scroll has its own page now which can be linked to.</li>
    </ul>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "About",
  components: {}
};
</script>

<style>
.about {
  margin: 30px;
}
</style>
