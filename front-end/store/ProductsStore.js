import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
const baseURL = "http://127.0.0.1:8000/api";

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
    async getProducts () {
      if (this.allProducts) {
        try {
          this.allProducts = await fetch(
            `${baseURL}/product_list/`
          ).then(response => response.json());
          this.filteredProducts = [
            ...this.allProducts.slice(0, this.filters.page * this.perPage)
          ];
        } catch (error) {
          console.log(error);
        }
      }
    },
    replaceSpecialChars (str) {
      str = str.replace(/[Á]/, 'a');
      str = str.replace(/[á]/, 'a');
      str = str.replace(/[É]/, 'e');
      str = str.replace(/[é]/, 'e');
      str = str.replace(/[Í]/, 'i');
      str = str.replace(/[í]/, 'i');
      str = str.replace(/[Ó]/, 'o');
      str = str.replace(/[ó]/, 'o');
      str = str.replace(/[Ú]/, 'u');
      str = str.replace(/[ú]/, 'u');
      return str;
    },
    search (s) {
      console.log(this.replaceSpecialChars(s));
      this.filters.s = this.replaceSpecialChars(s);
      this.filteredProducts = this.allProducts.filter(
        p =>
          this.replaceSpecialChars(p.name)
            .toLowerCase()
            .indexOf(this.filters.s.toLowerCase()) >= 0
      );
      this.filteredProducts = this.filteredProducts.slice(
        0,
        this.filters.page * this.perPage
      );
    },
    loadMore () {
      this.filters.page = this.filters.page + 1;
      this.filteredProducts = [
        ...this.allProducts.slice(0, this.filters.page * this.perPage)
      ];
    }
  }
});
