import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueSession from 'vue-session'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import store from './store'
import axios from 'axios'

Vue.use(BootstrapVue)
Vue.use(VueSession)
Vue.prototype.$axios = axios
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
