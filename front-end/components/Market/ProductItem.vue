<template>
  <article>
    <img :src="product.picture">
    <ul>
      <li>{{ product.name }}</li>
      <li>{{ product.description }}</li>
      <li>$ {{ product.price }}</li>
    </ul>
    <span>{{ product.update_at }}</span>
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
  @apply flex items-center h-2/4 m-3 p-3 bg-red-100 rounded-md;
}

img {
  @apply h-20 rounded-md;
}

ul {
  @apply ml-3 flex-1 w-64;
}

span {
  @apply self-start;
}
</style>