<template>
  <section>
    <div v-for="product in filteredProducts" :key="product.id">
      <IndexProductCard :product="product"/>
    </div>
  </section>
</template>
<script>
import { useProductsStore } from "../../store/ProductsStore";
import { mapState } from 'pinia'

export default {
  name: "IndexProductList",
  computed: {
    ...mapState(useProductsStore, ['allProducts', 'filteredProducts'])
  },
  setup () {
    const productsStore = useProductsStore();
    productsStore.getProducts();
  }
};
</script>
<style scoped>
section {
  @apply p-3 w-full flex flex-wrap justify-around;
}
</style>