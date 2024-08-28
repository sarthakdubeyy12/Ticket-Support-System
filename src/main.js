import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

const app = createApp(App)

// Set up Axios globally
app.config.globalProperties.$http = axios.create({
  baseURL: 'http://localhost:5176/'  // Adjust baseURL according to your backend server
})

app.use(router)
app.mount('#app')

