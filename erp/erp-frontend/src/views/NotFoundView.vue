<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 px-4">
    <div class="text-center max-w-md">
      
      <!-- 404 Number -->
      <h1 class="text-7xl font-bold text-gray-800">404</h1>

      <!-- Message -->
      <p class="mt-4 text-lg text-gray-600">
        Oops! The page you're looking for doesn't exist.
      </p>

      <p class="mt-2 text-sm text-gray-400">
        It might have been moved or deleted.
      </p>

      <!-- Button -->
      <router-link
        to="/"
        class="inline-block mt-6 px-6 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition"
      >
        Go Back Home
      </router-link>

      <!-- Optional secondary action -->
      <div class="mt-4">
        <button
          @click="$router.back()"
          class="text-sm text-gray-500 hover:text-gray-700 underline"
        >
          Go Back
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>

</script>