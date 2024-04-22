<script lang="ts" setup>
import { FetchError } from 'ofetch'

import type { Session } from '@/entities/Session'

import * as service from '@/services/AssignmentService'

const props = defineProps<{ item: Session }>()

const { students } = useForm()

const values = ref<any>({ session: props.item.id })

watch(
  () => props.item,
  (item) => {
    values.value = {
      session: item.id,
      student: undefined,
    }
  }
)

async function onSubmit(values: any) {
  const $toast = useNuxtApp().$toast

  try {
    await service.assign(values)

    props.item.assignments++

    $toast.success('Estudiante asignado correctamente.')
  } catch (error) {
    let message = 'Ocurrió un error al asignar el estudiante.'

    if (error instanceof FetchError && error.statusCode === 400) {
      message = error.data?.message
    }

    $toast.error(message)
  }
}
</script>

<template>
  <div class="card w-1/2 border-2">
    <div class="card-body pb-0">
      <h2 class="card-title">
        {{ item.name }}
      </h2>

      <div class="divider m-0"></div>

      <p>Fecha de Inicio: {{ formatDate(item.startDatetime) }}</p>
      <p>Horario: {{ formatSchedule(item.startDatetime, item.endDatetime) }}</p>
      <p>Cupo Disponible: {{ item.availability - item.assignments }}</p>

      <div class="mb-1"></div>

      <FormKit
        v-if="item.availability > item.assignments"
        type="form"
        v-model="values"
        :actions="false"
        @submit="onSubmit"
      >
        <FormKit
          type="hidden"
          name="session"
        />

        <FormKit
          type="select"
          name="student"
          label="Asignar Estudiante"
          placeholder="Ingrese el estudiante ha asignar"
          :options="students"
          validation="required"
          :validation-messages="{ required: 'Este campo es requerido.' }"
        />

        <FormKitMessages />

        <div class="card-actions mt-5 justify-end">
          <FormKit
            type="submit"
            label="Asignar"
            suffix-icon="submit"
            class="btn btn-primary"
          />
        </div>
      </FormKit>

      <p v-else>No hay cupo disponible para esta sesión.</p>
    </div>
  </div>
</template>
