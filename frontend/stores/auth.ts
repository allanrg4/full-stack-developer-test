type State = {
  access: string
  refresh: string
}

export const useAuthStore = defineStore('auth', {
  state: (): State => ({
    access: '',
    refresh: '',
  }),

  getters: {
    isAuthenticated: (state) => !!state.access,
  },
})
