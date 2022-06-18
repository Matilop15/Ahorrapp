<template>
  <article>
    <ProductCard :product="product"/>
    <hr>
    <ProductList />
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
    const product = await $http.$get(`https://api.nuxtjs.dev/beers/${params.id}`)
    return { product }
  }
};
</script>