import { createPinia } from "pinia";
import { createApp } from "vue";

import App from "./App.vue";
import router from "./router";

import "bootstrap";
import "./assets/main.scss";
import "./plugins/axios";

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
