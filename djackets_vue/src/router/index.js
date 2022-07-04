import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Product from '../views/Product.vue'
import Category from '../views/Category.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import Login from '../views/Login.vue'
import MyAccount from '../views/MyAccount.vue'
import CheckOut from '../views/CheckOut.vue'
import Success from '../views/Success.vue'


import store from '../store'



const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path:'/:category_slug/:product_slug/',
    name:'Product',
    component:Product
  },
  {
    path:'/:category_slug/',
    name:'Category',
    component:Category
  },
  {
    path:'/search/',
    name:'Search',
    component:Search,
  },
  {
    path:'/cart/',
    name:'Cart',
    component:Cart,
  },
  {
    path:'/sign-up/',
    name:'SignUp',
    component:SignUp
  },
  {
    path:'/login/',
    name:'Login',
    component:Login
  },
  {
    path:'/cart/success/',
    name:'Success',
    component:Success
  },
  {
    path:'/myaccount/',
    name:'MyAccount',
    component:MyAccount,
    beforeEnter(to,from,next){
      if(store.state.isAuthenticated){
        next(true)
      }
      else{
        next('/login/')
      }
    }
  },
  {
    path:'/checkout/',
    name:'CheckOut',
    component:CheckOut,
    beforeEnter(to,from,next){
      if(store.state.isAuthenticated){
        next(true)
      }
      else{
        next('/login/')
      }
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
