<script setup lang="ts">
import DarkMode from '@/components/DarkMode.vue';
import FooterMain from '@/components/FooterMain.vue';
import HeaderMain from '@/components/HeaderMain.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <DarkMode />

  <div class="container d-flex flex-column h-100">
    <HeaderMain />
    
    <main class="flex-shrink-0">
      <RouterView />
    </main>

    <FooterMain />
  </div>
</template>
