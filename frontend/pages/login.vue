<script lang="ts" setup>
const show = ref(false)
</script>

<template>
  <main class="flex h-screen w-screen items-center justify-center">
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
          :actions="false"
        >
          <div class="divider mb-2"></div>

          <h2 class="card-title mb-4">Inició de Sesión</h2>

          <FormKit
            type="text"
            name="username"
            label="Usuario"
            placeholder="Ingrese su nombre de usuario"
            validation="required"
          />

          <FormKit
            :type="show ? 'text' : 'password'"
            name="password"
            label="Contraseña"
            placeholder="Ingrese su contraseña"
            validation="required"
            :suffix-icon="show ? 'eye' : 'eyeClosed'"
            suffix-icon-class="hover:text-blue-500"
            @suffix-icon-click="() => (show = !show)"
          />

          <div class="card-actions justify-end">
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
