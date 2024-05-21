import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/WelcomeView.vue"),
    },
    {
      path: "/about",
      name: "about",
      component: () => import("@/views/AboutView.vue"),
    },
    {
      path: "/sign-in",
      name: "sign-in",
      component: () => import("@/views/auth/SignInView.vue"),
    },
    {
      path: "/sign-up",
      name: "sign-up",
      component: () => import("@/views/auth/SignUpView.vue"),
    },
  ],
});

export default router;
