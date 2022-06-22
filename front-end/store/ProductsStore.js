import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';

export const useProductsStore = defineStore('ProductsStore', {
  state: () => {
    return {
      allProducts: useStorage('allProducts', []),
      filteredProducts: [],
      filters: {
        s: '',
        page: 1
      },
      perPage: 10,
      lastPage: 0
    };
  },

  actions: {
    async getProducts() {
      if (this.allProducts) {
        try {
          this.allProducts = await fetch('https://www.ahorrapp.me/api/product_list/').then(
            (response) => response.json()
          );
          this.filteredProducts = [
            ...this.allProducts.slice(0, this.filters.page * this.perPage)
          ];
        } catch (error) {
          console.log(error);
        }
      }
    },
    search(s) {
      this.filters.s = s;
      this.filteredProducts = this.allProducts.filter(
        (p) => p.name.toLowerCase().indexOf(this.filters.s.toLowerCase()) >= 0
      );
      this.filteredProducts = this.filteredProducts.slice(
        0,
        this.filters.page * this.perPage
      );
    },
    loadMore() {
      this.filters.page = this.filters.page + 1;
      this.filteredProducts = [
        ...this.allProducts.slice(0, this.filters.page * this.perPage)
      ];
      console.log(this.filters.page + ' ' + this.lastPage)
      console.log(this.filters.page < this.lastPage)
    }
  }
});
