<template>
  <main>
    <div v-if="error.statusCode === 404">
      <img src="../static/logo.png" alt="">
      <span>404</span>
      <h1>Página no encontrada</h1>
      <NuxtLink to="/">Home page</NuxtLink>
    </div>
    <div v-else>
      <img src="../static/logo.png" alt="">
      <span>XD</span>
      <h1>A ocurrido un error</h1>
      <a href="https://www.ahorrapp.me">Home page</a>
    </div>
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

div {
  @apply flex flex-col items-center
}

a {
  @apply text-center mt-6 p-2 bg-red-300 w-32 h-10 text-gray-700 rounded-md shadow-md;
}
</style>