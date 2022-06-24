<template>
  <section id="compare-lists">
    <div class="listlist" v-for="group in groupedItemsMarket(allMarketProducts, grouped)" :key="group.id">
      <MyListMarketList :group='group' :total='getTotal(group, grouped)'/>
    </div>
  </section>
</template>

<script>
import { useAllMarketProductsStore } from "../../store/AllMarketProductsStore";
import { useListStore } from "../../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: "MyListCompare",
  computed: {
    ...mapState(useListStore, ['grouped', 'groupCount']),
    ...mapState(useAllMarketProductsStore, ['allMarketProducts'])
  },
  mounted () {
    const scrollContainer = document.querySelector("#compare-lists");

    scrollContainer.addEventListener("wheel", (evt) => {
        evt.preventDefault();
        scrollContainer.scrollLeft += evt.deltaY;
    });
  },
  methods: {
    groupedItemsMarket: (allProducts, groupedItems) => {
      const listMarket = []
      for (const key in groupedItems) {
        const filt = allProducts.filter((item) => item.product_id === parseInt(key))
        for (const item in filt){
          listMarket.push(filt[item])
        }
      }
      const tmpgroup = _.groupBy(listMarket, (item) => item.market_id)
      const temp = _.orderBy(tmpgroup, (item) => {
          return _.sumBy(item, 'price');
        })
      return temp
      // anterior >
      return _.groupBy(listMarket, (item) => item.market_id)
    },
    getTotal: (group, grouped) => {
      let total = 0
      for (const item in group) {
        total += group[item].price * grouped[group[item].product_id].length;
      }
      return total
    }
  }
}
</script>

<style scoped>
#compare-lists {
  @apply flex overflow-auto mt-4 mb-4;
}

</style>