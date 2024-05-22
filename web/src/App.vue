<script setup lang="ts">
import { useRoute } from 'vue-router';

import DarkMode from './components/DarkMode.vue';

const route = useRoute();
</script>

<template>
  <DarkMode />

  <component :is="route.meta.layoutComponent">
    <RouterView />
  </component>
</template>
