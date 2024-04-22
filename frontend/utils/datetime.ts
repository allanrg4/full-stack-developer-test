import { DateTime } from 'luxon'

export function getNow(): DateTime {
  return DateTime.now().setZone('America/Guatemala').setLocale('es')
}

export function formatDate(value: string): string {
  return DateTime.fromISO(value)
    .setZone('America/Guatemala')
    .setLocale('es')
    .toLocaleString(DateTime.DATE_HUGE)
}

export function formatTime(value: string): string {
  return DateTime.fromISO(value)
    .setZone('America/Guatemala')
    .setLocale('es')
    .toLocaleString(DateTime.TIME_SIMPLE)
}

export function formatSchedule(start: string, end: string): string {
  return `${formatTime(start)} a ${formatTime(end)}`
}
