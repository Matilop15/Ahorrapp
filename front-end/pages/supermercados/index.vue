<template>
  <section>
    <h1>Supermercados:</h1>
    <div v-for="market in allMarkets" :key="market.id">
      <NuxtLink :to="`/supermercados/${market.id}/`" >
        <MarketCard :market="market" />
      </NuxtLink>
    </div>
  </section>
</template>

<script>
import { useMarketsStore } from "../../store/MarketsStore";
import { mapState } from 'pinia'

export default {
  computed: {
    ...mapState(useMarketsStore, ['allMarkets'])
  },
};
</script>

<style scoped>
h1 {
  @apply text-xl m-3;
}
</style>