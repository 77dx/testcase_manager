// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import elementui from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

vue.use(elementui)
vue.use(vueresource)
Vue.config.productionTip = false

/* eslint-disable no-new */
new vue({
  el: '#app',
  router,
  render: h => h(app)
})

//new Vue({
//  el: '#app',
//  router,
//  components: { App },
//  template: '<App/>'
//})
