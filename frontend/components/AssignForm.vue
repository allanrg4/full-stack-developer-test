<script lang="ts" setup>
import type { Session } from '~/entities/Session'

type Props = {
  session: Session
}

const props = defineProps<Props>()

const { students } = useForm()
</script>

<template>
  <div class="card w-1/2 border-2">
    <div class="card-body pb-0">
      <FormKit
        type="form"
        :actions="false"
      >
        <h2 class="card-title mb-4">
          {{ props.session.name }}
        </h2>

        <div class="divider mb-2"></div>

        <p>Fecha de Inicio: {{ session.startDatetime }}</p>
        <p>Horario</p>
        <p>Cupo</p>

        <div class="mb-4"></div>

        <FormKit
          type="select"
          name="student"
          label="Asignar Estudiante"
          placeholder="Ingrese el estudiante ha asignar"
          :options="students"
          validation="required"
        />

        <FormKitMessages />

        <div class="card-actions mt-5 justify-end">
          <FormKit
            type="submit"
            label="Asignar"
            suffix-icon="submit"
            class="btn btn-primary"
            outer-classes="bg-red"
          />
        </div>
      </FormKit>
    </div>
  </div>
</template>
