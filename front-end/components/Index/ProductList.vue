<template>
  <section>
    <div v-for="product in filteredProducts" :key="product.id">
      <LazyIndexProductCard :product="product"/>
    </div>
    <button class="more-btn" v-if="!filters.s" v-show="filters.page <= lastPage" @click="loadMore()">Cargar más</button>
  </section>
</template>
<script>
import { useProductsStore } from "../../store/ProductsStore";
import { useAllMarketProductsStore } from "../../store/AllMarketProductsStore";
import { useMarketsStore } from "../../store/MarketsStore";
import { mapState } from 'pinia'

export default {
  name: "IndexProductList",
  computed: {
    ...mapState(useProductsStore, ['allProducts', 'filteredProducts', 'loadMore', 'filters', 'lastPage'])
  },
  setup () {
    const productsStore = useProductsStore();
    const AllMarketProductsStore = useAllMarketProductsStore();
    const MarketsStore = useMarketsStore();
    productsStore.getProducts();
    AllMarketProductsStore.getallMarketProducts();
    MarketsStore.getallMarkets();
    productsStore.lastPage = ~~(productsStore.allProducts.length / productsStore.perPage);
  }
};
</script>
<style scoped>
section {
  @apply p-3 w-full flex flex-wrap justify-around;
}

.more-btn {
  @apply bg-red-300 w-32 h-10 text-gray-700 rounded-md shadow-md;
}
</style>