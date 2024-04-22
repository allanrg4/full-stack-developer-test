import * as studentService from '@/services/StudentService'

type SelectOption = {
  value: any
  label: string
}

export function useForm() {
  const students = ref<SelectOption[]>([])

  onBeforeMount(async () => {
    const response = await studentService.all()

    students.value = response.map((item) => ({
      value: item.id,
      label: `${item.firstName} ${item.lastName}`,
    }))
  })

  return { students }
}
