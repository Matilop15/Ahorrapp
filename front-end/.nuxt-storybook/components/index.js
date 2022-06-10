export { default as Footer } from '../..\\components\\Footer.vue'
export { default as Header } from '../..\\components\\Header.vue'
export { default as PhoneMenu } from '../..\\components\\PhoneMenu.vue'
export { default as PhoneNav } from '../..\\components\\PhoneNav.vue'
export { default as PhoneNavButton } from '../..\\components\\PhoneNavButton.vue'
export { default as SearchBar } from '../..\\components\\SearchBar.vue'
export { default as Test } from '../..\\components\\test.vue'

// nuxt/nuxt.js#8607
function wrapFunctional(options) {
  if (!options || !options.functional) {
    return options
  }

  const propKeys = Array.isArray(options.props) ? options.props : Object.keys(options.props || {})

  return {
    render(h) {
      const attrs = {}
      const props = {}

      for (const key in this.$attrs) {
        if (propKeys.includes(key)) {
          props[key] = this.$attrs[key]
        } else {
          attrs[key] = this.$attrs[key]
        }
      }

      return h(options, {
        on: this.$listeners,
        attrs,
        props,
        scopedSlots: this.$scopedSlots,
      }, this.$slots.default)
    }
  }
}
