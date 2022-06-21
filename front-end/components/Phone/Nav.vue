<template>
  <nav class="phone-nav">
    <button class="nav-button">
      <NuxtLink to="/mi-lista">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
        </svg>
        <span id="count" v-if="count">{{count}}</span>
        <span class="tag">Mi Lista</span>
      </NuxtLink>
    </button>

    <button class="nav-button">
      <NuxtLink to="/">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <span class="tag">Buscar</span>
      </NuxtLink>
    </button>
    
    <button class="nav-button">
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
    ...mapState(useListStore, ['count'])
  }
}
</script>

<style scope>
.phone-nav {
  @apply fixed bottom-0 w-screen flex justify-around align-middle h-14 bg-white text-red-400 sm:hidden;
}

.tag {
  @apply hidden;
}

.nav-button {
  @apply h-full relative;
}

nav a.nuxt-link-exact-active{
  @apply bg-red-50 transition-all ease-in-out delay-200;
}

.nav-button > a.nuxt-link-exact-active .tag{
  @apply block font-bold;
}

.nav-button > a {
  @apply flex flex-col items-center w-32 h-full justify-center;
}



#count {
  @apply absolute top-2 right-10 text-sm font-semibold text-white bg-red-400 not-italic rounded-full w-4;
}

.nav-button > a.nuxt-link-exact-active #count {
  @apply top-0;
}
</style>