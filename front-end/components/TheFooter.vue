<template>
  <footer>
    <NuxtLink to="/about">
      <span>
        Sobre Nosotros
      </span>
    </NuxtLink>
  </footer>
</template>

<script lang="ts">

export default {
  name: 'TheFooter'
}
</script>

<style scoped>
footer {
  @apply mb-12;
}
</style>
