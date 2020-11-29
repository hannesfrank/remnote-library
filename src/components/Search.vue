<template>
  <div id="search" class="field has-addons is-fullwidth">
      <input
        class="input"
        type="text"
        placeholder="Filter scrolls..."
        v-bind:value="value"
        v-on:input="$emit('input', $event.target.value)"
      />
    <!-- <div class="control is-fullwidth">
    </div>
    <div class="control">
      <a class="button is-info is-light"> Filter </a>
    </div> -->
  </div>
</template>

<script>
export default {
  props: ["value"],
};
</script>

<style>
#search.field {
  padding: 10px;
  margin-bottom: 0;
}
</style>