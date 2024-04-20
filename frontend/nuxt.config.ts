// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: false,
  modules: ['@formkit/nuxt', '@pinia/nuxt'],
  css: ['~/assets/css/main.css'],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  formkit: {
    autoImport: true,
  },
  runtimeConfig: {
    public: {
      api: String(process.env.API_URL),
    },
  },
})
