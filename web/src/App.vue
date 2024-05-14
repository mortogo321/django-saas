<script setup lang="ts">
import DarkMode from '@/components/DarkMode.vue';
import FooterMain from '@/components/FooterMain.vue';
import HeaderMain from '@/components/HeaderMain.vue';
import { RouterView } from 'vue-router';
</script>

<template>
  <DarkMode />

  <div class="main-container container d-flex flex-column h-full">
    <HeaderMain />
    
    <main class="flex-grow-1 w-full">
      <RouterView />
    </main>

    <FooterMain />
  </div>
</template>
