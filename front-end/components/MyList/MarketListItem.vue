<template>
  <NuxtLink :to="`/productos/${product.product_id}/`">
    <article v-if="product.price">
      <h1 class="productname">{{ getProductName(allProducts, product.product_id) }}</h1>
      <p>$ {{ product.price }} x {{amount}}</p>
    </article>
  </NuxtLink>
</template>
<script>
import { useProductsStore } from "../../store/ProductsStore";
import { mapState } from 'pinia'

export default {
  name: 'MyListMarketListItem',
  props: ["product", "amount"],
  computed: {
  ...mapState(useProductsStore, ['allProducts'])
  },
  methods: {
    getProductName: (products, id) => {
      return products.filter((products) => products.id === id)[0].name
    },
    getProductImg: (products, id) => {
      return products.filter((products) => products.id === id)[0].img_url
    }
  }
}
</script>

<style scoped>
article {
  @apply flex justify-between m-3 p-3 bg-white rounded-md shadow-md;
}

p {
  @apply ml-3 text-gray-500;
}

.productname {
  @apply text-red-400 font-semibold;
}

span {
  @apply self-start text-gray-500;
}
</style>