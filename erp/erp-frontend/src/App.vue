<template>
  <router-view v-if="ready" />
</template>

<script setup>
import { ref, onMounted } from "vue"

const ready = ref(false)

onMounted(() => {
  // later you can validate token here
  ready.value = true
})
</script>