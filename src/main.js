import Vue from "vue";
import App from "./App.vue";

// import Buefy from "buefy";
// import "buefy/dist/buefy.css";
// Vue.use(Buefy);
import "bulma/css/bulma.css"

import router from './router'

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App)
}).$mount("#app");
