<template>
    <article>
      <NuxtLink :to="`/productos/${product.slug}/`">
        <img :src="product.image_url">
        <div id="description">
          <div>
            <h3>{{ product.name }} - {{ product.brewer }}</h3>
            <p>{{ product.size }}</p>
          </div>
        </div>
      </NuxtLink>
      <button @click="addItem(product)">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
        </svg>
      </button>
    </article>
</template>

<script>
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: 'IndexProductCard',
  props: ["product"],
  computed: {
    ...mapState(useListStore, ['addItem'])
  }
}
</script>

<style scoped>

article {
  @apply w-40 mb-4 p-3 rounded-xl bg-white shadow-md relative;
}

img {
  @apply w-full rounded-xl;
}

#description {
  @apply flex justify-between items-center mt-2;
}

h3 {
  @apply text-gray-600 font-bold;
}

p {
  @apply text-gray-500;
}

button {
  @apply w-8 h-8 bg-red-200 rounded-md self-start m-1 absolute bottom-1 right-1;
}

svg {
  @apply m-auto text-gray-700;
}
</style>