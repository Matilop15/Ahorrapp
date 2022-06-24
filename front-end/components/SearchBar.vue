<template>
  <span>
    <i>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-6 w-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        stroke-width="2"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
        />
      </svg>
    </i>
    <input autocomplete="off" type="text" name="Search" id="search-bar" placeholder="Buscar producto" @keyup="search($event.target.value)"/>
  </span>
</template>

<script>
import { useProductsStore } from "../store/ProductsStore";
import { mapState } from 'pinia'

export default {
  name: "SearchBar",
  computed: {
    ...mapState(useProductsStore, ['search'])
  }
};
</script>

<style scoped>
span {
  @apply w-full flex bg-white items-center rounded-md shadow-md
}
i {
  @apply p-2;
}

svg {
  @apply text-red-300;
}

#search-bar {
  @apply bg-white w-full h-10 text-lg rounded-md focus:outline-none;
}
</style>