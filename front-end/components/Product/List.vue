<template>
  <section>
    <div v-for="product in filterItems(allMarketProducts, id)" :key="product.id">
        <ProductItem :product="product" />
        <hr>
    </div>
  </section>
</template>
<script>
// /api/products/<product_id> todos los productos con el mismo id
import { useAllMarketProductsStore } from "../../store/AllMarketProductsStore";
import { mapState } from 'pinia'


export default {
  name: "ProductList",
  props: ["id"],
  computed: {
    ...mapState(useAllMarketProductsStore, ['allMarketProducts'])
  },
  methods: {
    filterItems: (items, id) => {
      const lodash = require("lodash");
      const filtitems =  items.filter((item) => item.product_id === id)
      return lodash.sortBy(filtitems, (e) => {
      return e.price
      })
    }
  }
};
</script>