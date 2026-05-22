<template>
  <div class="min-h-screen bg-gray-100 p-6">
    
    <!-- Header -->
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold">Client Dashboard</h1>

      <button
        @click="logout"
        class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600"
      >
        Logout
      </button>
    </div>

    <!-- Loading -->
    <div v-if="loading" class="text-gray-600">
      Loading user data...
    </div>

    <!-- Error -->
    <div v-if="error" class="text-red-500">
      {{ error }}
    </div>

    <!-- User Info -->
    <div v-if="user" class="bg-white p-4 rounded-xl shadow">
      <h2 class="text-lg font-semibold mb-2">User Info</h2>

      <pre class="text-sm bg-gray-50 p-3 rounded overflow-auto">
{{ user }}
      </pre>
    </div>

    <!-- Protected Data Example -->
    <div v-if="data" class="mt-6 bg-white p-4 rounded-xl shadow">
      <h2 class="text-lg font-semibold mb-2">Protected API Data</h2>

      <pre class="text-sm bg-gray-50 p-3 rounded overflow-auto">
{{ data }}
      </pre>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const loading = ref(true)
const error = ref("")
const user = ref(null)
const data = ref(null)

const token = localStorage.getItem("access_token")

// -------------------
// Logout
// -------------------
const logout = () => {
  localStorage.removeItem("access_token")
  localStorage.removeItem("refresh_token")
  localStorage.removeItem("user")

  router.replace("/")
}

// -------------------
// Fetch protected data
// -------------------
const fetchData = async () => {
  try {
    const res = await axios.get("http://erp.local/api/v1/health", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    data.value = res.data
  } catch (err) {
    error.value = "Failed to load protected data"
  }
}

// -------------------
// Decode JWT (optional quick view)
// -------------------
const decodeJWT = (token) => {
  try {
    const payload = token.split(".")[1]
    return JSON.parse(atob(payload))
  } catch (e) {
    return null
  }
}

onMounted(async () => {
  loading.value = true

  if (!token) {
    router.replace("/auth/login")
    return
  }

  // decode user from token (temporary until backend /me endpoint)
  user.value = decodeJWT(token)

  await fetchData()

  loading.value = false
})
</script>