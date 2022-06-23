<template>
  <div class="marketlists">
    <h1>{{getMarket(allMarkets, group[0].market_id)}}</h1>
    <div v-for="item in group" :key="item.id">
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
      return market.filter((market) => market.id === id)[0].name
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
  @apply w-80 ;
}

</style>