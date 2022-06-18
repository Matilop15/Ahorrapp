import { defineStore } from 'pinia';

export const useListStore = defineStore('ListStore', {
  state: () => {
    return {
      items: []
    };
  },

  getters: {
    count () {
      return this.items.length;
    }
  },

  actions: {
    addItems(count, item) {
      count = parseInt(count);
      for (let i = 0; i < count; i++) {
        this.items.push({ ...item });
      }
    }
  }
});
