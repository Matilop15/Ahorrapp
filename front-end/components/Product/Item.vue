<template>
  <div>
    <span>
      <p class="productprice">$ {{product.price}}</p>
      <h1>{{product.type}}</h1>
    </span>
    <p>{{product.updatedAt}}</p>
  </div>
</template>

<script>
export default {
  name: 'ProductCard',
  props: ["product"]
}
</script>

<style scoped>
div {
  @apply flex justify-between p-3 bg-white;
}
.productprice {
  @apply font-bold text-lg;
}
</style>