<template>
  <section>
    <MarketCard :market="market" />
    <MarketProductList :id="$route.params.id"/>
  </section>
</template>

<script>
// /api/providers/<id>

export default {
    head() {
        return {
            title: "Supermercado"
        };
    },
    async asyncData({ params, $http }) {
        const market = await $http.$get(`https://www.ahorrapp.me/api/markets/${params.id}`);
        return { market }
    }
};
</script>

<style scoped>

</style>