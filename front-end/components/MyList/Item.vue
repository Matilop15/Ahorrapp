<template>
  <article>
    <div class="desc-item">
      <img :src="item[0].image_url">
      <div>
        <h1>{{item[0].name}}</h1>
        <p>{{item[0].size}}</p>
      </div>
    </div>
    <div class="control-item">
      <button>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
      </button>
      <div class="amount-control">
        <button>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
        <p>1</p>
        <button>
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </button>
      </div>
    </div>
  </article>
</template>

<script>
export default {
  name: 'MyListItem',
  props: ["item"]
}
</script>

<style scoped>
article {
  @apply flex justify-between items-center m-4 p-2 bg-white shadow-md rounded-xl;
}

.desc-item {
  @apply flex items-center;
}

img {
  @apply w-20 h-20 rounded-xl;
}

.control-item {
  @apply flex flex-col justify-between items-end self-stretch;
}

.control-item > button {
  @apply items-end h-auto;
}

.amount-control {
  @apply flex;
}

</style>