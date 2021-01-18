import Vue from 'vue';
import Router from 'vue-router';
import Plates from './components/Plates.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/plate',
      name: 'Plates',
      component: Plates,
    },
  ],
});