<template>
  <button class="button" @click="copy">
    <span class="icon is-small">
      <i class="fas fa-copy"></i>
    </span>
    <span>{{ title }}</span>
  </button>
</template>
<script>
export default {
  props: ["content", "title"],
  methods: {
    copy: function() {
      navigator.clipboard.writeText(this.content);
    }
  }
};
</script>

<style lang="scss">
.button {
  vertical-align: initial;
}
</style>
