<script lang="ts" setup>
import type { Session } from '@/entities/Session'

type Props = {
  item: Session
  selected: boolean
}

const props = defineProps<Props>()
</script>

<template>
  <div
    class="card cursor-pointer border-2"
    :class="{ 'bg-cyan-100': selected, 'hover:bg-slate-200': !selected }"
  >
    <div class="card-body text-center">
      <span class="font-bold">
        {{ props.item.name }}
      </span>

      <span>
        {{ formatSchedule(item.startDatetime, item.endDatetime) }}
      </span>

      <span>
        {{ `Cupo: ${props.item.availability}` }}
      </span>
    </div>
  </div>
</template>
