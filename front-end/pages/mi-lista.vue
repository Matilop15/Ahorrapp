<template>
  <section>
    <h1>Mi Lista</h1>
    <div v-if="count === 0">
      <p id="empty">Tu lista esta vacia</p>
    </div>
    <div v-else v-for="item in grouped" :key="item.beer_id">
      <MyListItem :item="item"/>
    </div>
  </section>
</template>

<script>
import { useListStore } from "../store/ListStore";
import { mapState } from 'pinia';

export default {
  name: "MyList",
  computed: {
    ...mapState(useListStore, ['items', 'count', 'grouped'])
  }
}
</script>

<style scoped>
h1 {
  @apply text-center p-3 text-red-400 font-bold text-xl;
}

#empty {
  @apply flex h-20 justify-center items-center m-3;
}
</style>
