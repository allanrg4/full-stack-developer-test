<script lang="ts" setup>
const day = ref<number>()
const session = ref<number>()

definePageMeta({
  middleware: 'auth',
  layout: 'authenticated',
})
</script>

<template>
  <main class="container mx-auto mt-4">
    <div class="mb-10">
      <p class="mb-4 text-xl font-bold">Calendario</p>

      <div class="grid grid-cols-5 gap-5">
        <div
          v-for="i in 5"
          :key="i"
          class="card cursor-pointer border-2"
          :class="{ 'bg-cyan-100': day === i, 'hover:bg-slate-200': day !== i }"
          @click="day = i"
        >
          <div class="card-body text-center">
            <span>Martes</span>
            <span>16</span>
            <span>Abril</span>
          </div>
        </div>
      </div>
    </div>

    <div
      v-if="day"
      class="mb-10"
    >
      <p class="mb-4 text-xl font-bold">Sesiones Disponibles</p>

      <div class="grid grid-cols-5 gap-5">
        <div
          v-for="i in 5"
          :key="i"
          class="card cursor-pointer border-2"
          :class="{ 'bg-cyan-100': session === i, 'hover:bg-slate-200': session !== i }"
          @click="session = i"
        >
          <div class="card-body text-center">
            <span>Física 1</span>
            <span>8:10 am a 1:00 pm</span>
            <span>Cupo 10</span>
          </div>
        </div>
      </div>
    </div>

    <div v-if="session">
      <div class="card w-1/2 border-2">
        <div class="card-body pb-0">
          <FormKit
            type="form"
            :actions="false"
          >
            <h2 class="card-title mb-4">Curso: Física I</h2>

            <div class="divider mb-2"></div>

            <p>Fecha de Inicio</p>
            <p>Horario</p>
            <p>Cupo</p>

            <div class="mb-4"></div>

            <FormKit
              type="select"
              name="student"
              label="Asignar Estudiante"
              placeholder="Ingrese el estudiante ha asignar"
              :options="['Estudiante 1', 'Estudiante 2', 'Estudiante 3']"
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
    </div>
  </main>
</template>
