<script lang="ts" setup>
import { UserCircleIcon } from '@heroicons/vue/24/outline'

const auth = useAuthStore()

function onSignOut() {
  auth.access = ''
  auth.refresh = ''
}
</script>

<template>
  <div class="navbar bg-base-100 shadow-sm">
    <div class="container mx-auto">
      <div class="flex-1">
        <img
          src="https://www.galileo.edu/wp-content/themes/galileo-theme/img/logo-header.png"
          alt="Images de Universidad Galileo"
          draggable="false"
          class="w-20"
        />
      </div>

      <div class="flex-none gap-2">
        <div class="dropdown dropdown-end">
          <div
            tabindex="0"
            role="button"
            class="avatar btn btn-circle btn-ghost"
          >
            <UserCircleIcon class="w-8" />
          </div>

          <ul
            tabindex="0"
            class="menu dropdown-content menu-sm z-[1] mt-3 w-52 rounded-box bg-base-100 p-2 shadow"
          >
            <li>
              <a class="justify-between">
                Perfil
                <span class="badge">New</span>
              </a>
            </li>

            <li><a>Ajustes</a></li>

            <li>
              <a
                href="/login"
                @click="onSignOut"
                class="text-error"
              >
                Cerrar Sesión
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>
