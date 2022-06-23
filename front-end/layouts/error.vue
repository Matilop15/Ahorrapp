<template>
  <main>
    <div v-if="error.statusCode === 404">
    <img src="../static/logo.png" alt="">
    <span>404</span>
    <h1>Página no encontrada</h1>
    </div>
    <div v-else>
      <h1>A ocurrido un error</h1>
    </div>
    <NuxtLink to="/">Home page</NuxtLink>
  </main>
</template>

<script>
export default {
  props: ['error'],
  layout: 'other'
}
</script>

<style scoped>
main {
  @apply max-w-4xl m-auto flex flex-col items-center
}

span {
  @apply text-9xl
}

h1 {
  @apply text-center
}

a {
  @apply text-center m-5 p-2 bg-red-300 w-32 h-10 text-gray-700 rounded-md shadow-md;
}
</style>