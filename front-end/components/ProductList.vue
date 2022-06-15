<template>
  <section>
    <p v-if="$fetchState.pending">Cargando productos...</p>
    <p v-else-if="$fetchState.error">A ocurrido un error :(</p>
    <div v-else>
      <template v-for="product in products">
        <ProductCard :product="product" :key="product.id" />
      </template>
    </div>
  </section>
</template>
<script>
// /products va a devolver productos unicos
const sampleData = [
  {
    id: 1,
    name: "Arroz",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 2,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 3,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 4,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 5,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 6,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 7,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 8,
    name: "Yerba",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 9,
    name: "Fiambre",
    picture: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  }
];

export default {
  name: "ProductList",
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
section {
  @apply p-3;
}
div {
  @apply w-full flex flex-wrap justify-around;
}
</style>