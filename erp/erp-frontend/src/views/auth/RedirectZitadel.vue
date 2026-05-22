<script setup>
import { onMounted } from "vue"

onMounted(() => {
  window.location.href =
    "http://auth.local/oauth/v2/authorize" +
    "?client_id=373611437681082371" +
    "&response_type=code" +
    "&scope=openid profile email" +
    "&redirect_uri=http://localhost:5173/callback"
})
</script>