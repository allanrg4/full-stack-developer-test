<script lang="ts" setup>
import { DateTime } from 'luxon'

import type { Session } from '@/entities/Session'

type Props = {
  item: Session
  selected: boolean
}

const props = defineProps<Props>()

function getItemSchedule(item: Session) {
  return `${formatTime(item.startDatetime)} a ${formatTime(item.endDatetime)}`
}

function formatTime(datetime: string) {
  return DateTime.fromISO(datetime).setZone('America/Guatemala').setLocale('es').toFormat('HH:mm a')
}
</script>

<template>
  <div
    class="card cursor-pointer border-2"
    :class="{ 'bg-cyan-100': selected, 'hover:bg-slate-200': !selected }"
  >
    <div class="card-body text-center">
      <span>{{ props.item.name }}</span>
      <span>{{ getItemSchedule(props.item) }}</span>
      <span>{{ `Cupo: ${props.item.availability}` }}</span>
    </div>
  </div>
</template>
