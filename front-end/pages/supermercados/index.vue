<template>
  <section>
    <h1>Supermercados:</h1>
    <div v-for="market in markets" :key="market.id">
      <NuxtLink :to="`/supermercados/${market.name}/`" >
        <MarketCard :market="market" />
      </NuxtLink>
    </div>
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