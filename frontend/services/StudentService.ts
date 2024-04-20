import { useAPI } from '@/services/api'

import type { Student } from '@/entities/Student'

export function all() {
  return useAPI<Student[]>(`/students/`)
}
