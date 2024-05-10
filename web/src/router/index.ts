import HomeView from "@/views/HomeView.vue";
import { createRouter, createWebHistory } from "vue-router";

// TODO: get this from storage
const isAuthenticated = false;

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: () => import("@/views/auth/LoginView.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("@/views/AboutView.vue"),
    },
  ],
});

router.beforeEach(async (to) => {
  if (!isAuthenticated && to.name !== "login") {
    return { name: "login" };
  }
});

export default router;
