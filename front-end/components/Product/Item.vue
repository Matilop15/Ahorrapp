<template>
  <div v-if="product.price">
    <span>
      <p class="productprice">$ {{product.price}}</p>
      <h1>{{getMarket(allMarkets, product.market_id)}}</h1>
    </span>
    <p>{{product.update_date}}</p>
  </div>
</template>

<script>
import { useMarketsStore } from "../../store/MarketsStore";
import { mapState } from 'pinia'

export default {
  name: 'ProductCard',
  props: ["product"],
  computed: {
    ...mapState(useMarketsStore, ['allMarkets'])
  },
  methods: {
    getMarket: (market, id) => {
      return market.filter((market) => market.id === id)[0].name
    }
  }
}
</script>

<style scoped>
div {
  @apply flex justify-between p-3 bg-white;
}
.productprice {
  @apply font-bold text-lg;
}
</style>