<template>
  <article>
    <div>
      <h3>{{ market.name }}</h3>
      <ul>
        <li>{{ market.address }}</li>
        <li>{{ market.phone }}</li>
        <li><a :href="market.url">{{ market.url }}</a></li>
      </ul>
    </div>
    <img :src="market.picture" :alt="market.name">
  </article>
</template>
<script>
export default {
    name: 'MarketCard',
    props: ["market"]
}
</script>

<style scoped>
article {
  @apply flex justify-between h-36 m-3 p-3 bg-white rounded-xl shadow-md;
}

h3 {
  @apply text-lg font-bold text-red-400;
}

li {
  @apply text-gray-600;
}

div {
  @apply p-2 ;
}
img {
  @apply rounded-md;
}
</style>