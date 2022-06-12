<template>
    <NuxtLink :to="`/productos/${product.name}/`">
        <article>
            <img :src="product.picture">
            <div>
                <h5>{{ product.name }}</h5>
                <p>{{ product.description }}</p>
            </div>
        </article>
    </NuxtLink>
</template>

<script>
export default {
    name: 'ProductCard',
    props: ["product"]
}
</script>

<style scoped>
article {
    @apply border-2 w-40 mb-9;
}
img {
    @apply w-full;
}
</style>