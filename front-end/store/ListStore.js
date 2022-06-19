import { defineStore } from 'pinia';
import { groupBy } from 'lodash';

export const useListStore = defineStore('ListStore', {
  state: () => {
    return {
      items: []
    };
  },

  getters: {
    count: (state) => state.items.length,
    grouped: (state) => groupBy(state.items, (item) => item.beer_id),
    groupCount: (state) => Object.keys(state.grouped).length
  },

  actions: {
    addItem (item) {
      this.items.push({ ...item });
    }
  }
});
