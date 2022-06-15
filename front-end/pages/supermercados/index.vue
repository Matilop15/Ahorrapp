<template>
  <section>
    <h1>Supermercados:</h1>
    <template v-for="market in markets">
      <NuxtLink :to="`/supermercados/${market.name}/`" :key="market.id">
        <MarketCard :market="market" />
      </NuxtLink>
    </template>
  </section>
</template>

<script>
const sampleData = [
  {
    id: 1,
    name: "Ta-Ta",
    picture: "https://picsum.photos/200",
    address: "18 Julio",
    phone: "12444224",
    url: "https://www.tata.com.uy/"
  },
  {
    id: 2,
    name: "Disco",
    picture: "https://picsum.photos/200",
    address: "18 Julio",
    phone: "12444224",
    url: "https://www.tata.com.uy/"
  },
  {
    id: 3,
    name: "Geant",
    picture: "https://picsum.photos/200",
    address: "18 Julio",
    phone: "12444224",
    url: "https://www.tata.com.uy/"
  }
];

export default {
  data() {
    return {
      markets: [],
    };
  },
  async fetch() {
    this.markets = sampleData;
  },
};
</script>

<style scoped>
h1 {
  @apply text-xl m-3;
}
</style>