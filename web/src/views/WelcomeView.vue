<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';

const auth = useAuthStore();
</script>

<template>
  <div class="px-3 text-center">
    <h1>Welcome to KaliDocs</h1>
    <p class="lead">...</p>
    <p class="lead">
      <RouterLink :to="auth.isAuthenticated ? '/account' : '/auth/sign-in'" class="btn btn-lg btn-light">Get started</RouterLink>
    </p>
  </div>
</template>
