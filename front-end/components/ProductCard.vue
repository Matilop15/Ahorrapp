<template>
  <article>
    <img :src="product.UrlImg">
    <div id="description">
      <div>
        <h3>{{ product.Name }} - {{ product.Brand }}</h3>
        <p>{{ product.description }}</p>
      </div>
      <button>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
      </button>
    </div>
  </article>
</template>

<script>
export default {
  name: 'ProductCard',
  props: ["product"]
}
</script>

<style scoped>

article {
  @apply w-40 mb-4 p-3 rounded-xl bg-red-100 shadow-sm;
}

img {
  @apply w-full rounded-xl;
}

#description {
  @apply flex justify-between items-center mt-2;
}

p {
  @apply text-gray-500;
}

button {
  @apply w-10 h-10 bg-gray-50 rounded-md self-start mt-1;
}

svg {
  @apply m-auto;
}
</style>