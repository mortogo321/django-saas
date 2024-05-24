<script setup lang="ts">
import { useAuthStore } from '@/stores/auth';
import Swal from 'sweetalert2';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();

async function onLogout() {
    const result = await Swal.fire({
        title: "Are you leaving?",
        text: "Sing out!",
        icon: "warning",
        showCancelButton: true,
    });

    if (result.isConfirmed) {
        auth.setAuthentication({
            access: '',
            refresh: '',
        });
        router.push({ name: 'home' });
    }
}
</script>

<template>
    <header class="main-header w-full">
        <div class="py-3">
            <RouterLink to="/" class="navbar-brand">
                <h3 class="float-md-start mb-0">KaliDocs</h3>
            </RouterLink>

            <nav class="nav nav-masthead justify-content-center float-md-end">
                <RouterLink
                    to="/"
                    class="nav-link fw-bold py-1 px-0"
                    activeClass="active"
                    aria-current="page">
                    Home
                </RouterLink>
                <RouterLink
                    to="/about"
                    class="nav-link fw-bold py-1 px-0"
                    activeClass="active"
                    aria-current="page">
                    About
                </RouterLink>

                <template v-if="auth.isAuthenticated">
                    <RouterLink
                        to="/"
                        @click.prevent="onLogout"
                        class="nav-link fw-bold py-1 px-0"
                        aria-current="page">
                        Sign Out
                    </RouterLink>
                </template>
            </nav>
        </div>
    </header>
</template>