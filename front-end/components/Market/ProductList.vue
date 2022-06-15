<template>
  <section>
    <hr>
    <h2>Productos:</h2>
    <template v-for="product in products">
      <MarketProductItem :product="product" :key="product.id" />
    </template>
  </section>
</template>

<script>
// /supermercado/id/productos  trae productos de ese super
const sampleData = [
  {
    id: 1,
    name: "Arroz",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 2,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 3,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 4,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 5,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 6,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 7,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 8,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  },
  {
    id: 9,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 156,
    update_at: "21/7/22"
  }
];

export default {
  name: "MarketProductList",
  data() {
    return {
      products: [],
    };
  },
  async fetch() {
    this.products = sampleData;
  },
};
</script>

<style scoped>
h2 {
  @apply ml-3 text-lg font-bold;
}

hr {
  @apply w-40 border-black rounded-md m-auto;
}
</style>