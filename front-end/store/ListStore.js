import { defineStore } from 'pinia';
import { groupBy } from 'lodash';
import { useStorage } from '@vueuse/core';

export const useListStore = defineStore('ListStore', {
  state: () => {
    return {
      items: useStorage('items', [])
    };
  },

  getters: {
    count: (state) => state.items.length,
    grouped: (state) => groupBy(state.items, (item) => item.id),
    groupCount: (state) => (id) => {
      if (state.grouped[id]) {
        return state.grouped[id].length;
      } else {
        return false;
      }
    }
  },

  actions: {
    addItem(count, item) {
      for (let i = 0; i < count; i++) {
        this.items.push({ ...item });
      }
    },
    clearItem(id) {
      this.items = this.items.filter((item) => item.id !== id);
    },
    setItemAmount(count, item) {
      this.clearItem(item.id);
      this.addItem(count, item);
    },
    clearList() {
      this.items = [];
    }
  }
});
