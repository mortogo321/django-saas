<script setup lang="ts">
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { toast } from '@/plugins/sweetalert2';
import { activate } from '@/services/auth';
import type { ActivateForm } from '@/types/auth';

const route = useRoute();
const router = useRouter();

async function onActivate() {
    const form: ActivateForm = {
        uid: route.params.uid as string,
        token: route.params.token as string,
    };
    const { data } = await activate(form);

    toast.fire({
        icon: (typeof data === 'string' ? 'success' : 'error'),
        title: (data?.message || 'Account activated'),
        willClose: () => router.push('/auth/sign-in')
    });
}

onMounted(() => {
    onActivate();
});
</script>

<template>
    <div class="px-3 text-center">
        <h1>Activating...</h1>
        <p class="lead">
            <RouterLink to="/auth/sign-in" class="btn btn-lg btn-light">Sign In</RouterLink>
        </p>
    </div>
</template>
