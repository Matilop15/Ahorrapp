<template>
  <section>
    <div>
      <template v-for="product in products_sample">
        <IndexProductCard :product="product" :key="product.id" />
      </template>
    </div>
  </section>
</template>
<script>
import { useProductsSampleStore } from "../../store/products_sample";
import { mapState } from 'pinia'

export default {
  name: "IndexProductList",
  computed: {
    ...mapState(useProductsSampleStore, ['products_sample'])
  }
};
</script>
<style scoped>
section {
  @apply p-3;
}
div {
  @apply w-full flex flex-wrap justify-around;
}
</style>