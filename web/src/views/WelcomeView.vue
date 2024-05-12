<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';

const header = document.querySelector('.main-header');

onMounted(() => {
  if (header) {
    header.classList.add('mb-auto');
  }
});

onUnmounted(() => {
  if (header) {
    header.classList.remove('mb-auto');
  }
});
</script>

<template>
  <div class="cover-container mx-auto px-3 text-center">
    <h1>Welcome to KaliDocs</h1>
    <p class="lead">...</p>
    <p class="lead">
      <RouterLink to="/sign-in" class="btn btn-lg btn-light fw-bold border-white bg-white">Get started</RouterLink>
    </p>
  </div>
</template>
