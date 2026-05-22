import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import path from "path"

export default defineConfig({
  plugins: [vue()],

  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src")
    }
  },

  server: {
    host: "0.0.0.0",

    allowedHosts: ["erp.local"],

    watch: {
      usePolling: true,
      interval: 1000,
    },
  },
})