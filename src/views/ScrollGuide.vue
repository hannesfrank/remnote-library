<template>
  <div class="scroll-guide content">
    <h2 class="is-size-2">Make and Share a Scroll</h2>
    <figure class="image is-300x300 mt-0 is-pulled-right">
      <img
        src="../assets/scroll-bound.svg"
        alt="bound scroll"
      />
    </figure>
    <p class="is-size-4 is-family-primary">
      Comming Soon...
    </p>
    <p>
      Basically you
      <ol>
        <li>Copy the Scroll template</li>
        <li>Add your "magic", e.g. a some awesome CSS</li>
        <li>Describe it in <code>manifest.json</code> and</li>
        <li>Make a Pull Request on Github. If you plan to update it, add it as a submodule just referencing your own repo.</li>
      </ol>
    </p>
    <p>Later we'll add a backend with a database and a UI to publish scrolls.</p>
  </div>
</template>

<style scoped>
.scroll-guide {
  margin: 30px;
}

img {
  margin: 0 50px;
  width: 300px;
  height: 200px;
  object-fit: cover;
}
</style>
