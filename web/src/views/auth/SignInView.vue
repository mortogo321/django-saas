<script setup lang="ts">
import { useVuelidate } from '@vuelidate/core';
import { email, minLength, required } from '@vuelidate/validators';
import { computed, onMounted, onUnmounted, reactive } from 'vue';

import logo from '@/assets/logo.svg';
import { toast } from '@/plugins/sweetalert2';
import { signIn } from '@/services/auth';
import { singleView } from '@/utils';

onMounted(() => singleView());
onUnmounted(() => singleView(true));

const form = reactive({
    email: '',
    password: '',
    rememberMe: false,
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
    }
})

const v$ = useVuelidate(rules, form)

async function onSubmit() {
    const isValid = await v$.value.$validate()

    if (!isValid) {
        return
    }

    const { data } = await signIn(form);

    if (!data.success) {
        toast.fire({
            icon: 'error',
            title: data.message,
        });
    }
}
</script>

<template>
    <div class="w-1/3">
        <form @submit.prevent="onSubmit" class="form-floating">
            <img class="mb-4" :src="logo" alt="" width="72" height="57">
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

            <div class="form-floating mb-3">
                <input
                    type="email"
                    class="form-control"
                    :class="{ 'is-invalid': v$.email.$error }"
                    placeholder="name@example.com"
                    v-model="form.email">
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
                <div v-if="v$.password.$error" class="invalid-feedback">{{ v$.password.$errors[0].$message }}</div>
            </div>

            <div class="form-check text-start mb-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    Remember me
                </label>
            </div>
            <button class="btn btn-primary w-full py-2" type="submit">Sign in</button>
        </form>

        <div class="py-3 text-center">
            Don't have an account? <RouterLink to="/sign-up">Sign Up</RouterLink>
        </div>
    </div>
</template>
