// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// eslint-disable-next-line
/* eslint-disable */
import Vue from 'vue'
import App from './App'
//导入elementUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
//导入路由
import VueRouter from 'vue-router';
//导入我们写的路由
import router from './router'
import axios from 'axios'
// import VueAxios from 'vue-axios'
// import VueRouter from 'vue-router';

//使用ElementUI
Vue.use(ElementUI);

//使用路由
Vue.use(VueRouter);

axios.defaults.baseURL = 'http://localhost:8080/'
Vue.prototype.$axios = axios //全局挂载axios
// Vue.use(VueAxios,axios)

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router
})
