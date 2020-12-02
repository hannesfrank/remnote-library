<template>
  <button class="button is-small" @click="copy">
    <span class="icon is-small">
      <i class="fas fa-copy"></i>
    </span>
  </button>
</template>
<script>
export default {
  props: ["content"],
  methods: {
    copy: function() {
      navigator.clipboard.writeText(this.content);
    },
  },
};
</script>

<style lang="scss">
.button {
  vertical-align: initial;
}
</style>
