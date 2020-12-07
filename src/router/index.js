import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import ScrollGuide from "../views/ScrollGuide.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/library",
    name: "Library",
    // route level code-splitting
    // this generates a separate chunk (library.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "library" */ "../views/Library.vue")
  },
  {
    path: "/scroll-guide",
    name: "ScrollGuide",
    component: ScrollGuide
  }
];

const router = new VueRouter({
  // TODO: This does not work with gh-pages. Enable this when having a backend configured like this:
  // https://router.vuejs.org/guide/essentials/history-mode.html
  // mode: "history",
  base: process.env.BASE_URL,
  routes,
  linkActiveClass: "is-active-dropdown",
  linkExactActiveClass: "is-active"
});

export default router;
