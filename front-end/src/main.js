import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueSession from 'vue-session'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store from './store'
import axios from 'axios'

import Carousel3d from 'vue-carousel-3d'


Vue.use(BootstrapVue)
Vue.use(VueSession)
Vue.use(Carousel3d)
Vue.prototype.$axios = axios
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
