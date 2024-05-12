<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';

import logo from '@/assets/logo.svg';

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
    <div class="form-sign-in w-100 m-auto">
        <form>
            <img class="mb-4" :src="logo" alt="" width="72" height="57">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
            </div>

            <div class="form-check text-start my-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    Remember me
                </label>
            </div>
            <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-body-secondary">&copy;KaliDocs 2024</p>
        </form>
    </div>
</template>

<style lang="scss">
.form-sign-in {
    max-width: 330px;
    padding: 1rem;

    .form-floating:focus-within {
        z-index: 2;
    }

    input[type="email"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    input[type="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }
}
</style>