<script lang="ts" setup>
const auth = useAuthStore()

function onSignOut() {
  auth.access = ''
  auth.refresh = ''
}
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">GES</a>
    </div>

    <div class="flex-none gap-2">
      <div class="dropdown dropdown-end">
        <div
          tabindex="0"
          role="button"
          class="avatar btn btn-circle btn-ghost"
        >
          <div class="w-10 rounded-full">
            <img
              alt="Tailwind CSS Navbar component"
              src="https://daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg"
            />
          </div>
        </div>

        <ul
          tabindex="0"
          class="menu dropdown-content menu-sm z-[1] mt-3 w-52 rounded-box bg-base-100 p-2 shadow"
        >
          <li>
            <a class="justify-between">
              Profile
              <span class="badge">New</span>
            </a>
          </li>
          <li><a>Settings</a></li>
          <li>
            <a
              href="/login"
              @click="onSignOut"
            >
              Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
