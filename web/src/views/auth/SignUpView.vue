<script setup lang="ts">
import { useVuelidate } from '@vuelidate/core';
import { email, minLength, required, sameAs } from '@vuelidate/validators';
import { computed, nextTick, onMounted, reactive, ref } from 'vue';

import logo from '@/assets/logo.svg';
import { signUp } from '@/services/auth';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();
const autoFocus = ref();
const form = reactive({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
});
const rules = computed(() => {
    return {
        email: {
            required,
            email,
        },
        password: {
            required,
            minLength: minLength(4)
        },
        confirmPassword: sameAs(form.password),
    }
})
const v$ = useVuelidate(rules, form)

async function onSubmit() {
    const isValid = await v$.value.$validate()

    if (!isValid) {
        return
    }

    const { data } = await signUp(form);
    console.log({ data });
}

onMounted(() => {
    if (auth.isAuthenticated) {
        router.push('/dashboard');
    }

    nextTick(() => {
        autoFocus.value.focus();
    });
});
</script>

<template>
    <div class="w-1/3">
        <form @submit.prevent="onSubmit" class="form-floating">
            <img class="mb-4" :src="logo" alt="" width="72" height="57">
            <h1 class="h3 mb-3 fw-normal">Create an account</h1>

            <div class="form-floating mb-3">
                <input
                    type="email"
                    class="form-control"
                    :class="{ 'is-invalid': v$.email.$error }"
                    placeholder="name@example.com"
                    v-model="form.email"
                    ref="autoFocus">
                <label>Email address</label>
            </div>
            <div class="form-floating mb-3">
                <input
                    type="password"
                    class="form-control"
                    :class="{ 'is-invalid': v$.password.$error }"
                    placeholder="Password"
                    v-model="form.password">
                <label>Password</label>
            </div>

            <div class="form-floating mb-3">
                <input
                    type="password"
                    class="form-control"
                    :class="{ 'is-invalid': v$.confirmPassword.$error }"
                    placeholder="Confirm Password"
                    v-model="form.confirmPassword">
                <label>Password</label>
            </div>

            <button class="btn btn-primary w-full py-2" type="submit">Sign up</button>
        </form>

        <div class="py-3 d-flex flex-wrap justify-content-center align-items-center gap-1">
            Already have an account? <RouterLink to="/sign-in">Sign In</RouterLink>
            <span class="divider"></span>
            Forget your password? <RouterLink to="/">Reset Password</RouterLink>
        </div>
    </div>
</template>
