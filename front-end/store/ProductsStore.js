import { defineStore } from 'pinia';

export const useProductsStore = defineStore('ProductsStore', {

  state: () => {
    return {
      allProducts: [],
      filteredProducts: [],
      filters: {
        s: ''
      }
    };
  },

  actions: {
    async getProducts () {
      try {
        this.allProducts = await fetch('https://api.nuxtjs.dev/beers')
          .then((response) => response.json());
        this.filteredProducts = [...this.allProducts];
      } catch (error) {
        console.log(error);
      }
    },
    search (s) {
      this.filters.s = s;
      this.filteredProducts = this.allProducts.filter(p => p.name.toLowerCase().indexOf(this.filters.s.toLowerCase()) >= 0);
    }
  }

});
