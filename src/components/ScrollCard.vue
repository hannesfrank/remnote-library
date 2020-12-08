<template>
  <div class="scroll-card">
    <div class="card" @click="toggleDetails()">
      <div class="card-header">
        <div class="card-header-title">
          <span class="name">{{ name }}</span>
          <span class="author">
            <i class="fas fa-user" aria-hidden="true"></i>
            {{ authorName }}</span
          >
        </div>
      </div>
      <div class="card-content">
        <figure class="image">
          <img :src="thumbPath" alt="Placeholder image" />
        </figure>
      </div>
      <div class="card-footer">
        <span class="categories card-footer-item"
          ><div class="tags small">
            <span
              v-for="category in categories"
              :key="category"
              class="tag"
              :class="[`category-${category}`]"
              >#{{ category }}</span
            >
          </div>
        </span>
        <span class="stats card-footer-item">
          <span class="stat">
            <span class="icon is-small"
              ><i class="fas fa-angle-double-down" aria-hidden="true"></i
            ></span>
            <span class="value">{{ installCount }}</span>
          </span>
          <span class="stat">
            <span class="icon is-small mr-1"
              ><i class="fas fa-star fa-sm" aria-hidden="true"></i
            ></span>
            <span class="value">{{ rating }}</span>
          </span>
        </span>
      </div>
    </div>
    <div class="scroll-details modal" :class="{ 'is-active': showDetails }">
      <div class="modal-background" @click="toggleDetails()"></div>
      <!-- <div class="modal-content"> -->
      <div class="modal-card">
        <header class="modal-card-head">
          <div class="modal-card-title">
            <div class="shelf-icon icon is-large is-pulled-left m-1 mr-4">
              <i class="fas fa-palette fa-2x" aria-hidden="true"></i>
            </div>
            <div>
              <p class="title is-4">
                {{ name }}
              </p>
              <p class="subtitle is-size-7">
                {{ id }}
              </p>
            </div>
          </div>
          <button
            class="delete"
            aria-label="close"
            @click="toggleDetails()"
          ></button>
        </header>
        <section class="modal-card-body">
          <ScrollDetails :scrollData="scrollData" />
        </section>
        <footer class="modal-card-foot is-justify-content-flex-end">
          <router-link :to="{ name: 'ScrollDetails', params: { id } }">
            <button class="button is-primary">Details</button></router-link
          >
        </footer>
      </div>
      <!-- <button
        class="modal-close is-large"
        aria-label="close"
        @click="toggleDetails()"
      ></button> -->
    </div>
  </div>
</template>
<script>
import ScrollDetails from "./ScrollDetails.vue";

export default {
  components: {
    ScrollDetails
  },
  props: ["scrollData"],
  data() {
    return {
      publicPath: process.env.BASE_URL,
      showDetails: false
    };
  },

  methods: {
    toggleDetails: function() {
      this.showDetails = !this.showDetails;
    }
  },
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

.scroll-card .card {
  position: relative;
  width: 350px;
  height: fit-content;
  margin-bottom: 10px;
  box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.39);
  border-radius: 3px;
  cursor: pointer;

  .card-header {
    // TODO: Different colors for different shelves
    background-color: skyblue;
    // align-items: center;
    height: 35px;
    .card-header-title {
      display: flex;
      justify-content: space-between;
      flex-direction: row;

      .name {
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
      .name:hover {
        overflow: visible;
        text-overflow: unset;
      }

      .author {
        text-overflow: ellipsis;
        font-size: 10px;
        margin-left: 5px;
        flex-shrink: 0;
      }
    }
  }
  .card-content {
    padding: 0;

    figure {
      margin: 0;
    }

    figure.image {
      width: 350px;
      height: 200px;
    }
    img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
  }

  .card-footer {
    background-color: #f2f0f0;
    height: 30px;
    width: 100%;

    .stats {
      padding: 5px;

      .stat {
        white-space: nowrap;
        margin: 0 4px;

        span {
          vertical-align: middle;
        }
      }
    }

    .categories {
      padding: 5px;
      flex-grow: 4;
      justify-content: flex-start;
      .tag {
        font-size: 0.7rem;
        height: 20px;
      }
    }
  }
  &:hover {
    box-shadow: 0px 1px 4px 2px rgba(0, 0, 0, 0.39);
  }
}

.categories .tag {
  background-color: lightgrey;
}
.categories .tag.theme {
  background-color: rgb(147, 165, 255);
}
.categories .tag.dark {
  background-color: #333;
  color: #ddd;
}
.categories .tag.light {
  background-color: #fff;
  color: #333;
}
.categories .tag.rem-level {
  background-color: rgb(116, 248, 125);
}
.categories .tag.widget {
  background-color: rgb(62, 202, 71);
}
.categories .tag.formatting {
  background-color: rgb(204, 130, 241);
}
.categories .tag.sidebar {
  background-color: rgb(137, 204, 246);
}
.categories .tag.bullet-point {
  background-color: rgb(248, 101, 101);
}
.categories .tag.latex {
  background-color: rgb(227, 234, 0);
}

/*
.icon.installed {
  color: rgb(233, 117, 117);
}
.icon.not-installed {
  color: rgb(104, 212, 92);
}
.icon.report-problem {
  color: #ffda54;
}
*/
</style>
