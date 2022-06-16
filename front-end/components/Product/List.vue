<template>
  <section>
    <template v-for="product in products_sample">
        <ProductItem :product="product" :key="product.id" />
        <hr>
    </template>
  </section>
</template>
<script>
import { useProductsSampleStore } from "../../store/products_sample";
import { mapState } from 'pinia'

export default {
  name: "ProductList",
  computed: {
    ...mapState(useProductsSampleStore, ['products_sample'])
  }
};
</script>