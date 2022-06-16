<template>
  <section>
    <h1>Made By Getters</h1>
    <div v-for='gettersUser in getUsers' :key='gettersUser.id'>
    {{gettersUser.id}} {{gettersUser.name}}
    </div>
  </section>
</template>

<script>
// https://vueschool.io/articles/vuejs-tutorials/pinia-an-alternative-vue-js-store/
// import { useUserStore } from "../store/users";
// archivo en store start
import { useStorage } from '@vueuse/core'
import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    users: useStorage('users', [])
  }),
  getters: {
    getUsers (state) {
      return state.users;
    }
  },
  actions: {
    async fetchUsers () {
      try {
        this.users = await fetch('https://jsonplaceholder.typicode.com/users')
          .then((response) => response.json());
          console.log("fech");
      } catch (error) {
        console.log(error);
      }
    }
  }
});
// archivo en store end
import { mapState } from 'pinia'

export default {
  computed: {
    ...mapState(useUserStore, ['users', 'fetchUsers', 'getUsers'])
  },
  setup() {
    const { fetchUsers } = useUserStore()
    fetchUsers();
  }
}

</script>