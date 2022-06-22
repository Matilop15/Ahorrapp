<template>
  <article v-if="product.price">
    <img :src="getProductImg(allProducts, product.product_id)" :alt="product.name">
    <ul>
      <li class="productname">{{ getProductName(allProducts, product.product_id) }}</li>
      <li>$ {{ product.price }}</li>
    </ul>
    <span>{{ product.update_date }}</span>
  </article>
</template>
<script>
import { useProductsStore } from "../../store/ProductsStore";
import { mapState } from 'pinia'

export default {
  name: 'MarketProductItem',
  props: ["product"],
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
  @apply flex items-center h-2/4 m-3 p-3 bg-white rounded-md shadow-md;
}

img {
  @apply h-20 rounded-md;
}

ul {
  @apply ml-3 flex-1 w-64 text-gray-500;
}

.productname {
  @apply text-red-400 font-semibold;
}

span {
  @apply self-start text-gray-500;
}
</style>