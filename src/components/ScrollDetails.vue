<template>
  <div class="scroll-details tile is-ancestor is-vertical">
    <div class="tile is-parent">
      <div class="description tile is-child content">
        <p>
          {{ description }}
        </p>
        <p v-if="previewPath">
          <img class="preview" :src="previewPath" alt="Scroll preview" />
        </p>
      </div>
      <div class="about is-child">
        <!-- TODO: The about box shifts bad on small screens. -->
        <ul class="is-size-7 box m-0">
          <li>
            <span class="icon is-small"
              ><i class="fas fa-sm fa-user" aria-hidden="true"></i
            ></span>
            <span>{{ authorName }}</span>
          </li>
          <li>
            <span class="icon is-small"
              ><i class="fas fa-sm fa-external-link-alt" aria-hidden="true"></i
            ></span>
            <span><a :href="homepage">Homepage</a></span>
          </li>
          <li>
            <span class="icon is-small"
              ><i class="fas fa-sm fa-code-branch" aria-hidden="true"></i
            ></span>
            <span>{{ version }}</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="tile is-parent is-vertical">
      <div class="tile is-child content">
        <!-- <div class="tile is-child content">
                  <h4>Usage</h4>
                </div> -->
        <h4>Installation</h4>
        See
        <router-link to="/#custom-css-install-guide"
          >Custom CSS Install Guide</router-link
        >.
        <ol>
          <li>
            <CopyButton :content="customCSSBlock" title="Custom CSS Template" />
          </li>
          <li>
            <CopyButton :content="installCopy" title="CSS Code Block" />
          </li>
        </ol>
      </div>
    </div>
  </div>
</template>
<script>
import CopyButton from "./CopyButton.vue";

export default {
  components: {
    CopyButton
  },
  props: ["scrollData"],
  data() {
    return {
      publicPath: process.env.BASE_URL,
      showDetails: false
    };
  },
  methods: {},
  computed: {
    // Polymorphy: There could be cards for different kinds of scrolls.
    // Each type having its own attributes.
    // TODO: consider extracting the scrollData in an init method and not make so many computed properties
    authorName: function() {
      return (
        this.scrollData.author.name ||
        this.scrollData.author.email ||
        "Anonymous"
      );
    },
    categories: function() {
      return this.scrollData.categories;
    },
    customCSSBlock: function() {
      return this.scrollData.customCSSBlock;
    },
    description: function() {
      return this.scrollData.description;
    },
    homepage: function() {
      return this.scrollData.homepage;
    },
    id: function() {
      return this.scrollData.id;
    },
    install: function() {
      return this.scrollData.install;
    },
    installCopy: function() {
      // TODO: Assume only one install > copy for now. Refactor this when adding link scrolls.
      return this.install[0].content;
    },
    installCount: function() {
      return this.scrollData.installCount;
    },
    name: function() {
      return this.scrollData.name;
    },
    rating: function() {
      return this.scrollData.rating;
    },
    thumbPath: function() {
      return `${this.publicPath}${this.scrollData.thumb}`;
    },
    previewPath: function() {
      return this.scrollData.preview
        ? `${this.publicPath}${this.scrollData.preview}`
        : this.thumbPath;
    },
    version: function() {
      return this.scrollData.version || "--";
    }
  }
};
</script>

<style lang="scss">
/* Fix bug in bulma where there is a missing gap */

.tile.is-parent > .tile.is-child:not(:last-child) {
  margin-right: 1.5rem !important;
}

.scroll-details {
  .about {
    ul {
      list-style-type: none;
    }
  }
  img.preview {
    box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.2);
  }
}
</style>
