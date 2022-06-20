<template>
  <article>
    <img :src="product.image_url" :alt="product.name">
    <ul>
      <li class="productname">{{ product.name }}</li>
      <li>{{ product.size }}</li>
      <li>$ {{ product.price }}</li>
    </ul>
    <span>{{ product.updatedAt }}</span>
  </article>
</template>
<script>
export default {
    name: 'MarketProductItem',
    props: ["product"]
}
</script>

<style scoped>
article {
  @apply flex items-center h-2/4 m-3 p-3 bg-white rounded-md shadow-md;
}

img {
  @apply h-20 rounded-md;
}

ul {
  @apply ml-3 flex-1 w-64 text-gray-500;
}

.productname {
  @apply text-red-400 font-semibold;
}

span {
  @apply self-start text-gray-500;
}
</style>