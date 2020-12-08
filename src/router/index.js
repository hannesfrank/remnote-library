import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Featured from "../views/Featured.vue";
import ScrollGuide from "../views/ScrollGuide.vue";
import ScrollDetails from "../views/ScrollDetails.vue";

import scrolls from "../data.json";

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
    path: "/featured",
    name: "Featured",
    component: Featured
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
    path: "/scroll/:id",
    name: "ScrollDetails",
    component: ScrollDetails,
    props: route =>  ({
      scrollData: scrolls[route.params.id]
    })
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
  scrollBehavior: function(to, from, savedPosition) {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  },
  linkActiveClass: "is-active-dropdown",
  linkExactActiveClass: "is-active"
});

export default router;
