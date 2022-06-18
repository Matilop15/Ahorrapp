<template>
  <header>
    <img :src="product.image_url">
    <h1>{{ product.name }} - {{product.brewer}}</h1>
    <p>{{ product.size }}</p>
    <button>Agregar a la Lista</button>
  </header>
</template>

<script>
export default {
  name: 'ProductCard',
  props: ['product']
}
</script>

<style scoped>
header {
  @apply flex flex-col items-center justify-center h-96 m-5;
}

img {
  @apply h-48 w-48 rounded-xl shadow-sm;
}

h1 {
  @apply text-xl font-bold mt-5;
}

button {
  @apply bg-red-200 w-64 h-12 mt-5 shadow-sm rounded-xl;
}
</style>