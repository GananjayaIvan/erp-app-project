<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100 p-4">

    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">

      <div class="text-center mb-6">
        <h1 class="text-3xl font-bold text-gray-800">
          ERP System
        </h1>

        <p class="text-gray-500 mt-2">
          Sign in to continue
        </p>
      </div>

      <form
        @submit.prevent="handleLogin"
        class="space-y-4"
      >

        <div>
          <label class="block text-sm mb-2 text-gray-700">
            Email
          </label>

          <input
            v-model="email"
            type="email"
            class="w-full border rounded-xl px-4 py-3"
            placeholder="you@example.com"
          />
        </div>

        <div>
          <label class="block text-sm mb-2 text-gray-700">
            Password
          </label>

          <input
            v-model="password"
            type="password"
            class="w-full border rounded-xl px-4 py-3"
            placeholder="Enter password"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-black text-white py-3 rounded-xl font-semibold"
        >
          Login
        </button>

      </form>

    </div>

  </div>
</template>

<script setup>
import { ref } from "vue"
import { login } from "@/services/auth"

const email = ref("")
const password = ref("")

const handleLogin = async () => {

  try {

    const data = await login(
      email.value,
      password.value
    )

    console.log(data)

    localStorage.setItem(
      "access_token",
      data.access_token
    )

  } catch (err) {

    console.error(err)

  }
}
</script>