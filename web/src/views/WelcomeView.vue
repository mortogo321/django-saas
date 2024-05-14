<script setup lang="ts">
import { singleView } from '@/utils';
import { onMounted, onUnmounted } from 'vue';

onMounted(() => singleView());
onUnmounted(() => singleView(true));
</script>

<template>
  <div class="px-3 text-center">
    <h1>Welcome to KaliDocs</h1>
    <p class="lead">...</p>
    <p class="lead">
      <RouterLink to="/sign-in" class="btn btn-lg btn-light">Get started</RouterLink>
    </p>
  </div>
</template>
