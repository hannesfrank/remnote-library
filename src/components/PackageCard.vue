<template>
  <div class="scroll card">
    <div class="card-header">
      <div class="card-header-title">{{ title }}</div>
      <a href="#" class="card-header-icon" aria-label="more options">
        <span class="icon">
          <i class="fas fa-star" aria-hidden="true"></i>
          <span>{{ stars }}</span>
        </span>
      </a>
    </div>
    <div class="card-image">
      <figure class="image is-350x200">
        <img :src="thumb" alt="Placeholder image" />
      </figure>
    </div>
    <div class="card-footer">
      <span class="categories card-footer-item"
        ><div class="tags small">
          <span
            v-for="category in categories"
            :key="category"
            class="tag"
            :class="[category]"
            >#{{ category }}</span
          >
        </div>
      </span>
      <span class="actions card-footer-item">
        <span class="icon report-problem">
          <i class="fas fa-exclamation-triangle"></i>
        </span>
        <span v-if="installed" class="icon has-text-danger installed">
          <i class="fas fa-minus-circle" aria-hidden="true"></i>
        </span>
        <!-- <span v-else class="icon not-installed has-text-success">
          <i class="fas fa-plus-circle" aria-hidden="true"></i>
        </span> -->
        <span
          v-else
          @click="copyClip()"
          class="icon not-installed has-text-success"
        >
          <i class="fas fa-copy" aria-hidden="true"></i>
        </span>
      </span>
    </div>
  </div>
</template>
<script>
export default {
  props: ["title", "css", "stars", "categories", "installed", "thumb"],
  methods: {
    copyClip: function () {
      console.log(this.title);
      if (this.title == "Rating") {
        navigator.clipboard
          .writeText(`.rem[data-rem-tags~=one] .rem-text:before{
          content: '❤🤍🤍🤍🤍';
	
	background: #eee;
	padding: 4px;
	margin-bottom: 5px;
	border: 1px solid #333;
	display: inline-block;
}

.rem[data-rem-tags~=two] .rem-text:before{
  content: '❤❤❤🤍🤍';
	
	background: #eee;
	padding: 4px;
	margin-bottom: 5px;
	border: 1px solid #333;
	display: inline-block;
}

.rem[data-rem-tags~=three] .rem-text:before{
  content: '❤❤❤🤍🤍';
	background: #eee;
	padding: 4px;
	margin-bottom: 5px;
	border: 1px solid #333;
	display: inline-block;
}


.rem[data-rem-tags~=four] .rem-text:before{
  content: '❤❤❤❤🤍';
	background: #eee;
	padding: 4px;
	margin-bottom: 5px;
	border: 1px solid #333;
	display: inline-block;
}


.rem[data-rem-tags~=five] .rem-text:before{
  content: '❤❤❤❤❤';
	background: #eee;
	padding: 4px;
	margin-bottom: 5px;
	border: 1px solid #333;
	display: inline-block;
}`);
      } else {
        navigator.clipboard.writeText(`.document-title {
	font-family: "Forte";
}`);
      }
    },
  },
};
</script>

<style>
.scroll {
  position: relative;
  width: 350px;
  height: fit-content;
  margin-bottom: 10px;
  box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.39);
  border-radius: 3px;
}

.scroll:hover {
  box-shadow: 0px 1px 4px 2px rgba(0, 0, 0, 0.39);
}

.scroll .card-image img {
  object-fit: cover;
  width: 350px;
  height: 150px;
}

.scroll .card-header {
  background-color: #d2d0d0;
  height: 35px;
}
.card-header .card-header-icon .fa-star {
  position: relative;
  top: -2px;
  margin-right: 3px;
}

.scroll .card-footer {
  background-color: #f2f0f0;
  height: 30px;
  width: 100%;
  position: absolute;
  bottom: 0;
}

.card-footer .actions {
  justify-content: flex-end;
  padding: 5px;
}

.card-footer .icon {
  background-color: white;
  margin: 2px;
  box-shadow: 0 0 1px darkgrey;
  border-radius: 2px;
}

.card-footer .categories {
  padding: 5px;
  flex-grow: 4;
  justify-content: flex-start;
}

.card-footer .categories .tag {
  font-size: 0.7rem;
  height: 20px;
}

.card-footer .icon:hover {
  box-shadow: 0 0 2px black;
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

/* .icon.installed {
  color: rgb(233, 117, 117);
}
.icon.not-installed {
  color: rgb(104, 212, 92);
}
*/
.icon.report-problem {
  color: #ffda54;
}
</style>
