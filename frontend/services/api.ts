const config = useRuntimeConfig()

export const useAPI = $fetch.create({
  baseURL: config.public.api,
})
