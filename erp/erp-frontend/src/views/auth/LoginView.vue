<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">
      
      <!-- Header -->
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800">
          ERP System
        </h1>

        <p class="text-gray-500 mt-2">
          Sign in to continue
        </p>
      </div>

      <!-- Form -->
      <form
        @submit.prevent="handleLogin"
        class="space-y-4"
      >
        <!-- Email -->
        <div>
          <label class="block text-sm mb-2 text-gray-700">
            Email
          </label>

          <input
            v-model="email"
            type="email"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="you@example.com"
          />
        </div>

        <!-- Password -->
        <div>
          <label class="block text-sm mb-2 text-gray-700">
            Password
          </label>

          <input
            v-model="password"
            type="password"
            class="w-full border rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black"
            placeholder="Enter password"
          />
        </div>


        <!-- Forgot Password -->
        <RouterLink
        to="/auth/forgot-password"
        class="text-sm flex justify-end text-black hover:underline"
        >
          Forgot Password?
        </RouterLink>

        
        <!-- Login Button -->
        <button
          type="submit"
          class="w-full bg-black text-white py-3 rounded-xl font-semibold hover:bg-gray-800 transition"
        >
          Login
        </button>

      <!-- Register -->
      <div class="text-center text-sm text-gray-600 mt-4">
        Don't have an account?

        <RouterLink
          to="/auth/register"
          class="text-black font-semibold hover:underline ml-1"
        >
          Register
        </RouterLink>
      </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { login } from "@/services/auth"
import { useRouter } from "vue-router"

const router = useRouter()

const email = ref("")
const password = ref("")

const handleLogin = async () => {
  try {
    // validate credentials
    await login(email.value, password.value)

    // redirect after login
    router.push("/auth/redirect-zitadel")

  } catch (err) {
    console.error(err)
  }
}
</script>