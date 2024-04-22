<script lang="ts" setup>
import type { Session } from '@/entities/Session'

import * as service from '@/services/SessionService'

const props = defineProps<{ date: string }>()

const model = defineModel()

const sessions = ref<Session[]>([])

watch(
  () => props.date,
  async (date) => {
    sessions.value = await service.all({ date })
  }
)
</script>

<template>
  <div>
    <p class="mb-2 text-xl font-bold">Sesiones</p>

    <div
      v-if="sessions.length > 0"
      class="grid grid-cols-5 gap-5"
    >
      <SessionCard
        v-for="(item, i) in sessions"
        :key="item.id"
        :item="item"
        :selected="model === item.id"
        @click="model = item.id"
      />
    </div>

    <p v-else>No hay sesiones este día</p>
  </div>
</template>
