<script setup>
import { onMounted } from "vue"
import { useRouter } from "vue-router"

const router = useRouter()

onMounted(() => {
  const token = localStorage.getItem("access_token")
  const user = JSON.parse(localStorage.getItem("user") || "null")

  // no auth → go root
  if (!token) {
    router.replace("/")
    return
  }

  // role routing
  if (user?.role === "admin") {
    router.replace("/admin")
  } else {
    router.replace("/client")
  }
})
</script>