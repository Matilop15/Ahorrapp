<template>
  <article>
    <ProductCard :product="product"/>
    <hr>
    <ProductList :id="product.id"/>
  </article>
</template>

<script>
export default {
  head() {
    return {
      title: this.product.name
    };
  },
  async asyncData({ params, $http }) {
    const product = await $http.$get(`https://www.ahorrapp.me/api/product_list/${params.id}`)
    return { product }
  }
};
</script>