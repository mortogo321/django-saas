<script setup lang="ts">
import FooterMain from '@/components/FooterMain.vue';
import HeaderMain from '@/components/HeaderMain.vue';
</script>

<template>
    <div class="main-container container d-flex flex-column h-full">
        <HeaderMain />

        <main class="flex-grow-1 w-full">
            <slot />
        </main>

        <FooterMain />
    </div>
</template>