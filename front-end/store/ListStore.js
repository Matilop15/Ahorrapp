import { defineStore } from 'pinia';
import { groupBy, findLastKey } from 'lodash';
import { useStorage } from '@vueuse/core';

export const useListStore = defineStore('ListStore', {
  state: () => {
    return {
      items: useStorage('items', [])
    };
  },

  getters: {
    count: (state) => state.items.length,
    grouped: (state) => groupBy(state.items, (item) => item.beer_id),
    groupCount: (state) => Object.keys(state.grouped).length,
    itemAmount: (state) => (id) => Object.values(state.grouped[id]).length
  },

  actions: {
    addItem(item) {
      this.items.push({ ...item });
    },
    clearItem(id) {
      this.items = this.items.filter((item) => item.beer_id !== id);
    }
  }
});
