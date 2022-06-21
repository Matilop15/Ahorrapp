<template>
  <section>
    <MarketCard :market="market" />
    <MarketProductList />
  </section>
</template>

<script>
// /api/providers/<id>
const sampleData = {
    id: 1,
    name: "Ta-Ta",
    picture: "https://picsum.photos/200",
    address: "18 Julio",
    phone: "12444224",
    url: "https://www.tata.com.uy/"
  };

export default {
    head() {
        return {
            title: "Supermercado"
        };
    },
    data() {
        return {
            market: {}
        };
    },
    async fetch() {
        this.market = sampleData;
    }
};
</script>

<style scoped>

</style>