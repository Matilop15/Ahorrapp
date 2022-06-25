<template>
  <section>
    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3272.0245713251106!2d-56.190616948763896!3d-34.90583288028594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x959f81cd279bee3f%3A0xfbacc51b89e18218!2sTa-Ta!5e0!3m2!1sen!2suy!4v1655222297573!5m2!1sen!2suy" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </section>
</template>

<script>
export default {
  name: 'MarketMap'
}
</script>

<style scoped>
section {
  @apply h-64;
}
iframe {
  @apply w-full h-full;
}
</style>