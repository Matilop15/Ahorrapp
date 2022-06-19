<template>
  <nav>
    <button>
      <NuxtLink to="/mi-lista">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
        </svg>
        <span id="count" v-if="groupCount">{{groupCount}}</span>
        <span class="tag">Mi Lista</span>
      </NuxtLink>
    </button>

    <button>
      <NuxtLink to="/">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
        </svg>
        <span class="tag">Productos</span>
      </NuxtLink>
    </button>
    
    <button>
      <NuxtLink to="/supermercados">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
        </svg>
        <span class="tag">Supermercados</span>
      </NuxtLink>
    </button>
  </nav>
</template>

<script>
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: 'PhoneNav',
  computed: {
    ...mapState(useListStore, ['groupCount'])
  }
}
</script>

<style scope>
.tag {
  @apply hidden;
}

button {
  @apply h-full relative;
}

button > a.nuxt-link-exact-active{
  @apply text-red-400 bg-red-50 transition-all ease-in-out delay-200;
}

button > a.nuxt-link-exact-active .tag{
  @apply block font-bold;
}

button > a {
  @apply flex flex-col items-center w-32 h-full justify-center;
}

nav {
  @apply fixed bottom-0 w-screen flex justify-around align-middle h-14 bg-white text-red-300;
}

#count {
  @apply absolute top-2 right-10 text-sm font-semibold text-white bg-red-400 not-italic rounded-full w-4;
}

button > a.nuxt-link-exact-active #count {
  @apply top-0;
}
</style>