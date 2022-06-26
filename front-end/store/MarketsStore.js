import { defineStore } from 'pinia';
import { useStorage } from '@vueuse/core';
const baseURL = "http://127.0.0.1:8000/api";

export const useMarketsStore = defineStore('MarketsStore', {
  state: () => {
    return {
      allMarkets: useStorage('allMarkets', [])
    };
  },

  actions: {
    async getallMarkets () {
      try {
        this.allMarkets = await fetch(
          `${baseURL}/markets/`
        ).then((response) => response.json());
      } catch (error) {
        console.log(error);
      }
    }
  }
});
