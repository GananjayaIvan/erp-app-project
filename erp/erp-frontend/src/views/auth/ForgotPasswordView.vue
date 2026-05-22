<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100 p-4">
    
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">

      <!-- Header -->
      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800">
          Forgot Password
        </h1>

        <p class="text-gray-500 mt-2">
          Enter your email to reset your password
        </p>
      </div>

      <!-- Form -->
      <form
        @submit.prevent="handleForgotPassword"
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
            required
          />
        </div>

        <!-- Success Message -->
        <div
          v-if="successMessage"
          class="bg-green-100 text-green-700 px-4 py-3 rounded-xl text-sm"
        >
          {{ successMessage }}
        </div>

        <!-- Error Message -->
        <div
          v-if="errorMessage"
          class="bg-red-100 text-red-700 px-4 py-3 rounded-xl text-sm"
        >
          {{ errorMessage }}
        </div>

        <!-- Submit Button -->
        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-black text-white py-3 rounded-xl font-semibold hover:bg-gray-800 transition disabled:opacity-50"
        >
          {{ loading ? "Sending..." : "Send Reset Link" }}
        </button>

        <RouterLink
        to="/auth/login"
        class="text-sm text-black hover:underline"
        >
        Back to Login
        </RouterLink>

      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
// import { forgotPassword } from "@/services/auth"

const router = useRouter()

const email = ref("")
const loading = ref(false)
const successMessage = ref("")
const errorMessage = ref("")

const handleForgotPassword = async () => {
  try {
    loading.value = true
    successMessage.value = ""
    errorMessage.value = ""

    await new Promise(resolve => setTimeout(resolve, 1000))

    successMessage.value =
      "Password reset link has been sent to your email."

  } catch (err) {
    console.error(err)

    errorMessage.value =
      "Failed to send reset link. Please try again."

  } finally {
    loading.value = false
  }
}
</script>