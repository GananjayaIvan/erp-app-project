<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-6 rounded-xl shadow text-center w-80">
      <h1 class="text-lg font-semibold">Signing you in...</h1>

      <p v-if="loading" class="text-sm text-gray-500 mt-2">
        Please wait
      </p>

      <p v-if="error" class="text-sm text-red-500 mt-2">
        {{ error }}
      </p>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const loading = ref(true)
const error = ref("")

onMounted(async () => {
  const url = new URL(window.location.href)

  const code = url.searchParams.get("code")
  const oauthError = url.searchParams.get("error")
  const oauthErrorDesc = url.searchParams.get("error_description")

  // 1. Handle OAuth error
  if (oauthError) {
    console.error("OAuth error:", oauthError, oauthErrorDesc)
    error.value = oauthErrorDesc || oauthError
    loading.value = false

    setTimeout(() => router.replace("/"), 2000)
    return
  }

  // 2. Missing authorization code
  if (!code) {
    console.error("No authorization code returned")
    error.value = "Missing authorization code"
    loading.value = false

    setTimeout(() => router.replace("/"), 2000)
    return
  }

  try {
    // 3. Get PKCE verifier (IMPORTANT)
    const code_verifier = localStorage.getItem("pkce_verifier")

    if (!code_verifier) {
      throw new Error("Missing PKCE verifier. Please login again.")
    }

    // 4. Exchange code via backend (DO NOT call Zitadel directly here)
    const res = await axios.post(
      "http://erp.local/api/v1/auth/callback",
      {
        code,
        code_verifier,
        redirect_uri: import.meta.env.VITE_ZITADEL_REDIRECT_URI
      }
    )

    const data = res.data

    // 5. Store tokens
    localStorage.setItem("access_token", data.access_token)

    if (data.refresh_token) {
      localStorage.setItem("refresh_token", data.refresh_token)
    }

    if (data.user) {
      localStorage.setItem("user", JSON.stringify(data.user))
    }

    // 6. Clean up PKCE verifier (security best practice)
    localStorage.removeItem("pkce_verifier")

    // 7. Redirect to app
    router.replace("/client")

  } catch (err) {
    console.error("Login failed:", err)

    error.value =
      err?.response?.data?.detail ||
      err.message ||
      "Authentication failed"

    loading.value = false

    setTimeout(() => router.replace("/"), 2000)
  }
})
</script>