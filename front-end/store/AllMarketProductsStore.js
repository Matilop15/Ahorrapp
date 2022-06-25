import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';

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
          'https://www.ahorrapp.me/api/products/'
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
    }
  }
});
