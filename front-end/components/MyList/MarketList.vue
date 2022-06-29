<template>
  <div class="marketlists">
    <div class="super-img">
      <img :src="getMarket(allMarkets, group[0].market_id).img_url" :alt="getMarket(allMarkets, group[0].market_id).name">
    </div>
    <div class="super-item" v-for="item in group" :key="item.id">
      <MyListMarketListItem :product='item' :amount='groupCount(item.product_id)'/>
    </div>
    <h2>Total: ${{total}}</h2>
  </div>
</template>

<script>
import { useMarketsStore } from "../../store/MarketsStore";
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia'

export default {
  name: 'MyListMarketList',
  props: ['group', 'total'],
  computed: {
    ...mapState(useListStore, ['groupCount']),
    ...mapState(useMarketsStore, ['allMarkets'])
  },
  methods: {
    getMarket: (market, id) => {
      return market.filter((market) => market.id === id)[0]
    }
  }
}
</script>

<style scoped>
h1 {
  @apply text-center p-3 text-red-400 font-bold text-xl;
}

h2 {
  @apply text-center p-3 text-gray-700 font-bold text-xl;
}

.marketlists {
  @apply flex flex-col items-center border-2 m-1 rounded-xl border-red-100;
}

.super-img {
  @apply h-40 bg-white w-full rounded-xl flex justify-center items-center;
}

img {
  @apply w-40 rounded-xl;
}

.super-item {
  @apply w-full;
}

</style>