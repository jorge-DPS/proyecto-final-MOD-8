import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import './assets/main.css'  // o './index.css' según el nombre que hayas usado
const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
