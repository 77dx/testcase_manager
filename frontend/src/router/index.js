// eslint-disable-next-line
/* eslint-disable */
import Vue from 'vue'
// 导入路由
import Router from 'vue-router'
//导入登录页
import Login from '../views/Login'


//使用路由
Vue.use(Router);

export default new Router({
  routes: [
    //登录页
    {
      //通过login访问
      path: '/login',
      //路由名
      name: 'Login',
      //使用的组件是我们导入的Login
      component: Login
    }
  ]
})
