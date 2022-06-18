<template>
  <section>
    <hr>
    <h2>Productos:</h2>
    <div v-for="product in products" :key="product.id">
      <MarketProductItem :product="product" />
    </div>
  </section>
</template>

<script>
// /api/products/providers/<providers_id>/ productos  trae productos de ese super

export default {
  data: () => ({
    products: []
  }),
  async fetch() {
    this.products = await this.$http.$get('https://api.nuxtjs.dev/beers');
  }
};
</script>

<style scoped>
h2 {
  @apply ml-3 text-lg font-bold;
}

hr {
  @apply w-40 border-black rounded-md m-auto;
}
</style>