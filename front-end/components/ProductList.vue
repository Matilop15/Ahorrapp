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
    Name: "Arroz",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 2,
    Name: "Yerba",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 3,
    Name: "Fiambre",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 4,
    Name: "Yerba",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 5,
    Name: "Fiambre",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 6,
    Name: "Yerba",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 7,
    Name: "Fiambre",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 8,
    Name: "Yerba",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
    description: "1kg",
    price: 100
  },
  {
    id: 9,
    Name: "Fiambre",
    Brand: "Marca",
    UrlImg: "https://picsum.photos/200",
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
  }
  // data() {
  //   return {
  //     products: []
  //   }
  // },
  // async fetch() {
  //   this.products = await fetch(
  //     'http://www.ahorrapp.me/api/product/1'
  //   ).then(res => res.json())
  // }
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