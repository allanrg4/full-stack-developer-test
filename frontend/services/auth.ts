import { useAPI } from '@/services/api'

type LoginParams = {
  username: string
  password: string
}

type LoginResponse = {
  access: string
  refresh: string
}

export function signIn(params: LoginParams) {
  return useAPI<LoginResponse>(`/auth/token/`, {
    method: 'POST',
    body: params,
  })
}
