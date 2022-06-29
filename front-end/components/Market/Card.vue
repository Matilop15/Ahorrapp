<template>
  <article>
    <div>
      <h3>{{ market.name }}</h3>
      <ul>
        <li><a :href="market.url">{{ market.url }}</a></li>
      </ul>
    </div>
      <img :src="market.img_url" alt="">
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
  @apply flex justify-between items-center h-36 m-3 p-3 bg-white rounded-xl shadow-md;
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
  @apply w-32 rounded-md;
}
</style>