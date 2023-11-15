// //import './assets/main.css'

// import { createApp } from 'vue'
// import App from './App.vue'

// //Vue.prototype.$http = axios

// createApp(App).mount('#app')

import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import store from './store/index.js'

import 'element-plus/dist/index.css'



const app = createApp(App)

app.use(ElementPlus)
app.use(store)
app.mount('#app')
