import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/LandingPage.vue")
  },
  // AUTH (public)
  {
    path: "/auth/login",
    name: "Login",
    component: () => import("@/views/auth/LoginView.vue"),
    meta: { public: true }
  },
  {
    path: "/auth/register",
    name: "Register",
    component: () => import("@/views/auth/RegisterView.vue"),
    meta: { public: true }
  },
  {
    path: "/auth/forgot-password",
    name: "ForgotPassword",
    component: () => import("@/views/auth/ForgotPasswordView.vue"),
    meta: { public: true }
  },
  {
    path: "/auth/callback",
    name: "Callback",
    component: () => import("@/views/auth/CallbackView.vue"),
    meta: { public: true }
  },

  //PUBLIC CLIENT PAGE
  {
    path: "/client",
    name: "Client",
    component: () => import("@/views/client/ClientView.vue"),
    meta: { public: true }
  },

  //ADMIN (protected)
  {
    path: "/admin",
    name: "Admin",
    component: () => import("@/views/admin/AdminView.vue"),
    meta: { requiresAuth: true }
  },

  // ROOT → redirect explicitly (IMPORTANT)
  {
    path: "/",
    redirect: "/",
    meta: { public: true }
  },

  //404 fallback
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("@/views/NotFoundView.vue"),
    meta: { public: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

/**
 *GLOBAL AUTH GUARD
 */
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token")
  const isPublic = to.meta.public
  const requiresAuth = to.meta.requiresAuth

  //block protected pages if not logged in
  if (requiresAuth && !token) {
    return next("/auth/login")
  }

  // prevent logged-in users from seeing login page again
  if (to.path === "/auth/login" && token) {
    return next("/admin")
  }

  next()
})

export default router