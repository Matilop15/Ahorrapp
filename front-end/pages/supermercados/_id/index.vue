<template>
  <section>
    <MarketCard :market="market" />
    <MarketProductList :id="$route.params.id"/>
    <a :href="'/supermercados/'+ $route.params.id +'/#go-top'">
      <button id="top-btn" title="Go to top">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M5 11l7-7 7 7M5 19l7-7 7 7" />
        </svg>
      </button>
    </a>
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
#top-btn {
  @apply fixed bottom-16 md:bottom-5 right-4 z-10 bg-red-200 p-3 rounded-md
}
</style>