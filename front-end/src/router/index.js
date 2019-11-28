import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '@/views/Login.vue' // @ => src 폴더
import Signup from '@/views/Signup.vue'
import Welcome from '@/views/Welcome.vue'
import Search from '@/views/Search.vue'
import MovieDetail from '@/views/MovieDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'welcome',
    component: Welcome
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/movie/:id',
    name: 'movieDetail',
    component: MovieDetail,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router