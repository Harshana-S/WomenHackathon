import Vue from 'vue'
import App from './App'
import router from './router'
// import store from "./store";

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
//import 'bootstrap-vue/dist/bootstrap-vue.css'

import "vue-material-design-icons/styles.css"
import VueCollapse from 'vue2-collapse'

import { Icon }  from 'leaflet'
import 'leaflet/dist/leaflet.css'

Vue.use(VueCollapse)
Vue.config.productionTip = false
import vueScrollto from 'vue-scrollto'

Vue.use(vueScrollto)

delete Icon.Default.prototype._getIconUrl;

Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

Vue.use(BootstrapVue)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
