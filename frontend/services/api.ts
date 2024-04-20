const config = useRuntimeConfig()

export const useAPI = $fetch.create({
  baseURL: config.public.api,
  onRequest({ options }) {
    const auth = useAuthStore()

    if (auth.isAuthenticated)
      options.headers = {
        ...options.headers,
        Authorization: `Bearer ${auth.access}`,
      }
  },
})
