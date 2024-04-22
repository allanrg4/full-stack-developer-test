<script lang="ts" setup>
import { DateTime } from 'luxon'

import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/24/outline'

const model = defineModel()

const now = DateTime.now().setZone('America/Guatemala').setLocale('es')
const currentWeek = ref(0)

const currentWeekDays = computed(() => {
  let week = now.plus({ weeks: currentWeek.value })
  let current = week.startOf('week')
  let endWeek = week.endOf('week')

  const days = []

  while (current <= endWeek) {
    days.push({
      day: current.day,
      month: current.monthLong,
      weekDay: current.weekdayLong,
      date: current.toISODate(),
      value: current.toFormat('yyyy-MM-dd'),
    })

    current = current.plus({ days: 1 })
  }

  return days
})

onBeforeMount(() => {
  model.value = now.toFormat('yyyy-MM-dd')
})
</script>

<template>
  <div class="flex items-center gap-4">
    <button
      class="btn btn-ghost"
      @click="() => currentWeek--"
    >
      <ChevronLeftIcon class="h-5 w-5" />
    </button>

    <div class="grid flex-1 grid-cols-7 gap-4">
      <div
        v-for="(item, i) in currentWeekDays"
        :key="i"
        class="card cursor-pointer border-2"
        :class="{ 'bg-cyan-100': model === item.value, 'hover:bg-slate-200': model !== item.value }"
        @click="model = item.value"
      >
        <div class="card-body text-center capitalize">
          <span>{{ item.day }}</span>
          <span>{{ item.weekDay }}</span>
          <span>{{ item.month }}</span>
        </div>
      </div>
    </div>

    <button
      class="btn btn-ghost"
      @click="() => currentWeek++"
    >
      <ChevronRightIcon class="h-5 w-5" />
    </button>
  </div>
</template>
