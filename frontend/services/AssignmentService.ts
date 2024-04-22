import { useAPI } from '@/services/api'

type AssignParams = {
  session: number
  student: number
}

export function assign(params: AssignParams) {
  return useAPI(`/assignments/`, {
    method: 'POST',
    body: params,
  })
}
