<template>
  <section>
    <div v-for="product in filteredProducts" :key="product.id">
      <LazyIndexProductCard :product="product"/>
    </div>
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

    const { scrollHeight } = document.documentElement;
    if (scrollHeight > 520) {
      productsStore.loadMore()
    } 
    window.addEventListener('scroll', function () {
      const {
          scrollTop,
          scrollHeight,
          clientHeight
      } = document.documentElement;

      if (scrollTop + clientHeight >= scrollHeight - 5 || scrollHeight < 520) {
          productsStore.loadMore()
      }
    })
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