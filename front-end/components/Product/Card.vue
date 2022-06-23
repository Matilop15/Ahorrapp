<template>
  <header>
    
    <img :src="product.img_url">
    <h1>{{ product.name }}</h1>
    <button @click="addItem('1' ,product)">
    <span class="amount-list" v-if="groupCount(product.id)">{{ groupCount(product.id) }}</span>
    Agregar a la Lista
    </button>
  </header>
</template>

<script>
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: 'ProductCard',
  props: ['product'],
  computed: {
    ...mapState(useListStore, ['addItem', 'groupCount'])
  }
}
</script>

<style scoped>
header {
  @apply flex flex-col items-center justify-center h-96 m-5;
}

img {
  @apply h-48 w-auto rounded-xl shadow-sm;
}

h1 {
  @apply text-xl font-bold mt-5 text-center;
}

button {
  @apply relative bg-red-200 w-64 h-12 mt-5 shadow-sm rounded-xl;
}

.amount-list {
  @apply absolute -right-2 -top-2 text-center font-semibold text-white bg-red-400 not-italic rounded-full w-6;;
}
</style>