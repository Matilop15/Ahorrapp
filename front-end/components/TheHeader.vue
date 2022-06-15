<template>
  <header>
    <NuxtLink to="/">
      <h1>Ahorrapp</h1>
    </NuxtLink>
  </header>
</template>

<script>
export default {
  name: 'TheHeader'
}
</script>

<style scoped>
header {
  @apply w-screen p-3 sticky top-0 bg-white;
}
</style>