import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Vue from 'vue'

//!Global axios defaults
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

//!Vue
createApp(App).use(store).use(router,axios).mount('#app')
