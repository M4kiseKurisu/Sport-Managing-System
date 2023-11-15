// //import './assets/main.css'

// import { createApp } from 'vue'
// import App from './App.vue'
// import axios from 'axios'
// //Vue.prototype.$http = axios

// createApp(App).mount('#app')

import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'



const app = createApp(App)

app.use(ElementPlus)
app.mount('#app')
