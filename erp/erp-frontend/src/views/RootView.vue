<script setup>
import { onMounted } from "vue"
import { useRouter } from "vue-router"
import axios from "axios"

const router = useRouter()

onMounted(async () => {
  const token = localStorage.getItem("access_token")

  if (!token) {
    router.replace("/client")
    return
  }

  try {
    const res = await axios.get("http://erp.local/api/v1/auth/me", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    const roles = res.data.roles || []

    if (roles.includes("admin")) {
      router.replace("/admin")
    } else {
      router.replace("/client")
    }

  } catch (err) {
    console.error(err)
    localStorage.removeItem("access_token")
    router.replace("/client")
  }
})
</script>