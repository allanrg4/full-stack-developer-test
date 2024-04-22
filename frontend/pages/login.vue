<script lang="ts" setup>
import * as authService from '@/services/AuthService'

const auth = useAuthStore()

const show = ref(false)
const errors = ref<string[]>([])

async function onSubmit(values: any) {
  try {
    const response = await authService.signIn(values)

    auth.access = response.access
    auth.refresh = response.refresh

    navigateTo('/')
  } catch (error) {
    errors.value = ['Usuario o contraseña incorrectos']
  }
}
</script>

<template>
  <main class="flex h-screen w-screen items-center justify-center bg-base-200">
    <div class="card w-[25vw] bg-white pt-10 shadow-xl">
      <figure>
        <img
          src="https://www.galileo.edu/wp-content/themes/galileo-theme/img/logo-header.png"
          alt="Images de Universidad Galileo"
          draggable="false"
        />
      </figure>

      <div class="card-body pb-0">
        <FormKit
          type="form"
          :errors="errors"
          :actions="false"
          @submit="onSubmit"
        >
          <div class="divider mb-2"></div>

          <h2 class="card-title mb-4">Inició de Sesión</h2>

          <FormKit
            type="text"
            name="username"
            label="Usuario"
            placeholder="Ingrese su nombre de usuario"
            validation="required"
            :validation-messages="{ required: 'Este campo es requerido.' }"
          />

          <FormKit
            :type="show ? 'text' : 'password'"
            name="password"
            label="Contraseña"
            placeholder="Ingrese su contraseña"
            validation="required"
            :validation-messages="{ required: 'Este campo es requerido.' }"
            :suffix-icon="show ? 'eye' : 'eyeClosed'"
            suffix-icon-class="hover:text-blue-500"
            @suffix-icon-click="() => (show = !show)"
          />

          <FormKitMessages />

          <div class="card-actions mt-5 justify-end">
            <FormKit
              type="submit"
              label="Iniciar Sesión"
              suffix-icon="submit"
              class="btn btn-primary"
              outer-classes="bg-red"
            />
          </div>
        </FormKit>
      </div>
    </div>
  </main>
</template>
