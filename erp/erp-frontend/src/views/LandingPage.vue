<template>
  <div class="min-h-screen bg-gray-50 text-gray-800">

    <!-- NAVBAR -->
    <header class="flex items-center justify-between px-8 py-5 bg-white shadow-sm">
      <div class="text-xl font-bold tracking-tight">
        SmartERP
      </div>

      <div class="flex gap-4 items-center">
        <button
          @click="goLogin"
          class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Login
        </button>
      </div>
    </header>

    <!-- HERO -->
    <section class="px-8 py-20 text-center bg-gradient-to-br from-blue-50 to-white">
      <h1 class="text-4xl md:text-5xl font-bold mb-4">
        Modern ERP System for Growing Businesses
      </h1>

      <p class="text-lg text-gray-600 max-w-2xl mx-auto mb-8">
        Manage finance, operations, HR, and reporting in one integrated platform.
        Built for speed, scalability, and clarity.
      </p>

      <div class="flex justify-center gap-4">
        <button
          @click="goLogin"
          class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
        >
          Get Started
        </button>

        <button
          class="px-6 py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition"
        >
          Learn More
        </button>
      </div>
    </section>

    <!-- FEATURES -->
    <section class="px-8 py-16 max-w-6xl mx-auto">
      <h2 class="text-2xl font-bold text-center mb-10">
        Core Modules
      </h2>

      <div class="grid md:grid-cols-3 gap-6">

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">Finance</h3>
          <p class="text-gray-600 text-sm">
            Manage income, expenses, budgeting, and financial reports in real time.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">HR Management</h3>
          <p class="text-gray-600 text-sm">
            Employee records, attendance, payroll, and performance tracking.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">Operations</h3>
          <p class="text-gray-600 text-sm">
            Workflow automation, task tracking, and operational dashboards.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">Inventory</h3>
          <p class="text-gray-600 text-sm">
            Track stock levels, purchases, and warehouse movement.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">Sales</h3>
          <p class="text-gray-600 text-sm">
            CRM, invoices, quotations, and customer management.
          </p>
        </div>

        <div class="bg-white p-6 rounded-xl shadow-sm">
          <h3 class="font-semibold text-lg mb-2">Analytics</h3>
          <p class="text-gray-600 text-sm">
            Real-time dashboards and business intelligence reports.
          </p>
        </div>

      </div>
    </section>

    <!-- BENEFITS -->
    <section class="bg-white py-16 px-8">
      <div class="max-w-4xl mx-auto text-center">
        <h2 class="text-2xl font-bold mb-6">
          Why SmartERP?
        </h2>

        <p class="text-gray-600 mb-10">
          Built for modern businesses that need clarity, control, and automation without complexity.
        </p>

        <div class="grid md:grid-cols-3 gap-6 text-left">

          <div>
            <h4 class="font-semibold mb-1">⚡ Fast</h4>
            <p class="text-sm text-gray-600">Optimized workflows for speed and efficiency.</p>
          </div>

          <div>
            <h4 class="font-semibold mb-1">🔒 Secure</h4>
            <p class="text-sm text-gray-600">ZITADEL-based authentication and role control.</p>
          </div>

          <div>
            <h4 class="font-semibold mb-1">📊 Scalable</h4>
            <p class="text-sm text-gray-600">Designed to grow with your business needs.</p>
          </div>

        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="px-8 py-20 text-center bg-blue-600 text-white">
      <h2 class="text-3xl font-bold mb-4">
        Ready to streamline your business?
      </h2>

      <p class="mb-6 text-blue-100">
        Sign in to access your ERP dashboard and start managing your operations.
      </p>

      <button
        @click="goLogin"
        class="px-6 py-3 bg-white text-blue-600 font-semibold rounded-lg hover:bg-gray-100 transition"
      >
        Login to Dashboard
      </button>
    </section>

    <!-- FOOTER -->
    <footer class="py-6 text-center text-sm text-gray-500 bg-gray-100">
      © {{ new Date().getFullYear() }} SmartERP. All rights reserved.
    </footer>

  </div>
</template>

<script setup>
import { useRouter } from "vue-router"

const router = useRouter()

const goLogin = () => {
  router.push("/auth/login")
}
</script>