<template>
  <header>
    <NuxtLink to="/">
      <div id="logo">
        <img src="../static/logo.png" alt="">
        <h1>Ahorrapp</h1>
      </div>
    </NuxtLink>
    <nav id="desktop-nav">
      <NuxtLink to="/mi-lista">
        <span id="list">
          <span id="desktop-nav-count" v-if="groupCount">{{groupCount}}</span>
          <span>Mi Lista</span>
        </span>
      </NuxtLink>
    
      <NuxtLink to="/supermercados">
        <span>Supermercados</span>
      </NuxtLink>
  </nav>
  </header>
</template>

<script>
import { useListStore } from "../store/ListStore";
import { mapState } from 'pinia';
export default {
  name: 'TheHeader',
  computed: {
    ...mapState(useListStore, ['groupCount'])
  }
}
</script>

<style scoped>

header {
  @apply m-3 mb-0 flex justify-between items-center;
}

#desktop-nav {
  @apply text-red-300 hidden sm:flex;
}

#desktop-nav > a{
  @apply ml-4;
}

#logo{
  @apply flex items-center;
}

#logo img {
  @apply w-14
}

#logo h1 {
  @apply text-red-300 text-2xl;
  font-family: Archive
}

#list {
  @apply relative
}

#desktop-nav-count {
  @apply absolute top-0 -left-5 text-sm text-center font-semibold text-white bg-red-400 not-italic rounded-full w-4;
}
</style>