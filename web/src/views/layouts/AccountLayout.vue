<script setup lang="ts">
import FooterMain from '@/components/FooterMain.vue';
import HeaderMain from '@/components/HeaderMain.vue';
import SidebarMain from '@/components/SidebarMain.vue';
</script>

<template>
    <div class="main-container container d-flex flex-column h-full">
        <HeaderMain />

        <main class="flex-grow-1 w-full d-flex gap-3">
            <SidebarMain />
            <div class="w-full border">
                <RouterView />
            </div>
        </main>

        <FooterMain />
    </div>
</template>