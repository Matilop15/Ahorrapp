<template>
    <article>
      <NuxtLink :to="`/productos/${product.id}/`">
        <span class="amount-list" v-if="groupCount(product.id)">{{ groupCount(product.id)}}</span>
        <img :src="product.img_url" :alt="product.name">
        <div id="description">
          <div>
            <h3>{{ product.name }}</h3>
          </div>
        </div>
      </NuxtLink>
      <button @click="addItem('1' ,product)">
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
    ...mapState(useListStore, ['addItem', 'groupCount'])
  }
}
</script>

<style scoped>

article {
  @apply w-40 h-44 mb-4 p-3 rounded-xl bg-white shadow-md relative;
}

img {
  @apply w-full rounded-xl;
}

#description {
  @apply flex justify-between items-center mt-2;
}

h3 {
  @apply text-gray-600 font-bold w-28;
  overflow:hidden;
  -webkit-box-orient: vertical;
  display: -webkit-box;
  text-overflow: ellipsis;
  -webkit-line-clamp: 2;
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

.amount-list {
  @apply absolute text-center font-semibold text-white bg-red-400 not-italic rounded-full w-6;;
}
</style>