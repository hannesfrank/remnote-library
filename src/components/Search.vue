<template>
  <div class="search">
    <div class="buttons are-small px-3 pt-3 m-0">
      <div
        class="button is-info"
        :class="{
          'is-active': category === selectedCategory,
          'is-outlined': selectedCategory && category != selectedCategory
        }"
        v-for="category in sortedCategories"
        :key="category"
        @click="selectCategory(category)"
      >
        #{{ category }}
      </div>
      <span>You can also search with <code>#category-name</code></span>
    </div>
    <div id="search" class="field has-addons is-fullwidth mt-0">
      <input
        class="input"
        type="text"
        placeholder="Filter scrolls..."
        v-model="value"
      />
      <!-- <div class="control is-fullwidth">
    </div>
    <div class="control">
      <a class="button is-info is-light"> Filter </a>
    </div> -->
    </div>
  </div>
</template>

<script>
// TODO: I'd like to have the category buttons reflected on the query and vice versa.
//  - if a button is pressed, insert the text into the input
//  - if the category is changed or deleted deselect the button and optionally reselect another
export default {
  props: ["query", "categories"],
  data: function() {
    return {
      value: "",
      selectedCategory: ""
    };
  },
  methods: {
    selectCategory: function(category) {
      if (this.selectedCategory === category) {
        this.selectedCategory = "";
      } else {
        this.selectedCategory = category;
      }
      this.updateQuery();
    },
    updateQuery: function() {
      const categoryQuery = this.selectedCategory
        ? "#" + this.selectedCategory
        : "";
      const newQuery = categoryQuery + this.value;
      this.$emit("input", newQuery);
    }
  },
  computed: {
    sortedCategories: function() {
      return [...this.categories].sort();
    }
  },
  watch: {
    value: function(val) {
      this.updateQuery();
    }
  }
};
</script>

<style>
#search.field {
  padding: 10px;
  margin-bottom: 0;
}
</style>
