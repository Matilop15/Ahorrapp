import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';

export const useMarketsStore = defineStore('MarketsStore', {
  state: () => {
    return {
      allMarkets: useStorage('allMarkets', [])
    };
  },

  actions: {
    async getallMarkets() {
      try {
        this.allMarkets = await fetch(
          'https://www.ahorrapp.me/api/markets/'
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
    }
  }
});
