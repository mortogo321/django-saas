import { useAuthStore } from "@/stores/auth";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/views/WelcomeView.vue"),
      meta: {
        layout: "SingleLayout",
      },
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
      meta: {
        layout: "SingleLayout",
      },
    },
    {
      path: "/sign-up",
      name: "sign-up",
      component: () => import("@/views/auth/SignUpView.vue"),
      meta: {
        layout: "SingleLayout",
      },
    },
    // {
    //   path: "/account",
    //   component: () => import("@/views/account/AccountView.vue"),
    //   meta: {
    //     layout: "AccountLayout",
    //     requiresAuth: true,
    //   },
    //   children: []
    // },
  ],
});

router.beforeEach(async (to) => {
  const auth = useAuthStore();
  let layout = null;

  try {
    layout = await import(`@/views/layouts/${to.meta?.layout}.vue`);
  } catch (error) {
    layout = await import(`@/views/layouts/MainLayout.vue`);
  }

  to.meta.layoutComponent = layout.default;

  if (to.meta?.requiresAuth && !auth.isAuthenticated && to.name !== "sign-in") {
    return { name: "sign-in" };
  }
});

export default router;
