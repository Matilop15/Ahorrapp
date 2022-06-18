<template>
  <section>
    <div v-for="product in products" :key="product.id">
        <ProductItem :product="product" />
        <hr>
    </div>
  </section>
</template>
<script>
// /api/products/<product_id> todos los productos con el mismo id
export default {
  name: "ProductList",
  data: () => ({
    products: []
  }),
  async fetch() {
    this.products = await this.$http.$get('https://api.nuxtjs.dev/beers');
  }
};
</script>