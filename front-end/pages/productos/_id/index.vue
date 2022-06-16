<template>
  <article>
    <ProductCard :product="product"/>
    <hr>
    <ProductList />
  </article>
</template>

<script>
const sample = {
        "ProductId": 1,
        "Name": "arroz",
        "UrlImg": "https://www.recetasderechupete.com/wp-content/uploads/2019/08/Arroz-blanco-768x527.jpg",
        "Brand": "bluepatna",
        "desc": "1kg"
    }
export default {
  head() {
    return {
      title: this.product.Name
    };
  },
  mounted() {
    const id = this.$route.params.id.split("-")
    console.log(id[1]);
  },
  asyncData() {
    let data = sample;
    return {
      product: data
    };
  },
  data() {
    return {
      product: []
    };
  }
};
</script>