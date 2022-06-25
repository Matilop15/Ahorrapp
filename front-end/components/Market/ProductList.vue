<template>
  <section>
    <hr>
    <h2>Productos:</h2>
    <div v-for="product in filterItems(allMarketProducts, id)" :key="product.id">
      <MarketProductItem :product="product" />
    </div>
  </section>
</template>

<script>
import { useAllMarketProductsStore } from "../../store/AllMarketProductsStore";
import { mapState } from 'pinia'

export default {
  name: 'MarketProductList',
  props: ['id'],
  computed: {
    ...mapState(useAllMarketProductsStore, ['allMarketProducts'])
  },
  methods: {
    filterItems: (items, id) => {
      return items.filter((item) => item.market_id === parseInt(id))
    }
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