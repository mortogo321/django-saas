<script setup lang="ts">
import logo from '@/assets/logo.svg';
import Swal from 'sweetalert2';
import { onMounted, onUnmounted } from 'vue';

import { singleView } from '@/utiles';

onMounted(() => singleView());
onUnmounted(() => singleView(true));

function onSubmit() {
    Swal.fire({
        title: 'Error!',
        text: 'Do you want to continue',
        icon: 'error',
        confirmButtonText: 'Cool'
    });
}
</script>

<template>
    <div class="w-1/3">
        <form @submit.prevent="onSubmit">
            <img class="mb-4" :src="logo" alt="" width="72" height="57">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating mb-3">
                <input
                    type="email"
                    class="form-control"
                    placeholder="name@example.com"
                    required>
                <label>Email address</label>
            </div>
            <div class="form-floating mb-3">
                <input
                    type="password"
                    class="form-control"
                    placeholder="Password"
                    required>
                <label>Password</label>
            </div>

            <div class="form-check text-start my-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    Remember me
                </label>
            </div>
            <button class="btn btn-primary w-full py-2" type="submit">Sign in</button>
        </form>
    </div>
</template>
