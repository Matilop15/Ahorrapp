import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
const baseURL = "http://127.0.0.1:8000/api";

export const useAllMarketProductsStore = defineStore('AllMarketProductsStore', {
  state: () => {
    return {
      allMarketProducts: useStorage('allMarketProducts', [])
    };
  },

  actions: {
    async getallMarketProducts () {
      try {
        this.allMarketProducts = await fetch(
          `${baseURL}/products/`
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
    }
  }
});
