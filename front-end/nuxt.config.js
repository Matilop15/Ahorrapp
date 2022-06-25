export default {
  // Disable server-side rendering: https://go.nuxtjs.dev/ssr-mode
  ssr: false,

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Ahorrapp',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: 'Comparador de precios de Supermercados'
      },
      { name: 'format-detection', content: 'telephone=no' },
      {
        name: 'author',
        content: 'Bruno Rodríguez, Matias Lopéz, Angel Piva, Şahin MERİÇ'
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: ['~/assets/main.css'],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
    '@nuxt/postcss8',
    // Nuxt 2 only:
    // https://composition-api.nuxtjs.org/getting-started/setup#quick-start
    '@nuxtjs/composition-api/module',
    // https://pinia.vuejs.org/
    '@pinia/nuxt',
    // https://vueuse.org/
    '@vueuse/nuxt',
    '@nuxtjs/pwa'
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxt/http'
  ],

  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // Workaround to avoid enforcing hard-coded localhost:3000: https://github.com/nuxt-community/axios-module/issues/308
    baseURL: '/'
  },

  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      name: 'Ahorrapp',
      short_name: 'Ahorrapp',
      lang: 'es',
      description: 'Comparador de precios de Supermercados',
      background_color: '#fef2f2',
      start_url: '/',
      theme_color: '#fef2f2',
      display_override: ['window-control-overlay', 'minimal-ui'],
      display: 'display'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {}
};
