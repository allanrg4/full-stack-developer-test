<script lang="ts" setup>
import type { Session } from '~/entities/Session'

const date = ref<string>()
const session = ref<Session>()

definePageMeta({
  middleware: 'auth',
  layout: 'authenticated',
})
</script>

<template>
  <main class="container mx-auto mt-4 flex flex-col gap-10">
    <WeeklyCalendar v-model="date" />

    <SessionRow
      v-if="date"
      v-model="session"
      :date="date"
    />

    <AssignForm
      v-if="session"
      :session="session"
    />
  </main>
</template>
