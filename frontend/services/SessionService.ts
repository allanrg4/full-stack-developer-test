import { useAPI } from '@/services/api'

import type { Session } from '@/entities/Session'

type AllQuery = {
  date: string
}

export function all(query: AllQuery) {
  return useAPI<Session[]>(`/sessions/`, { query })
}
