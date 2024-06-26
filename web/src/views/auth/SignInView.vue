<script setup lang="ts">
import { useVuelidate } from '@vuelidate/core';
import { email, minLength, required } from '@vuelidate/validators';
import { computed, nextTick, onMounted, reactive, ref } from 'vue';

import logo from '@/assets/logo.svg';
import ButtonLoading from '@/components/ButtonLoading.vue';
import { toast } from '@/plugins/sweetalert2';
import { signIn } from '@/services/auth';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();
const autoFocus = ref();
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
            minLength: minLength(8)
        },
    }
})
const v$ = useVuelidate(rules, form)
const loading = ref(false);

async function onSubmit() {
    const isValid = await v$.value.$validate()

    if (!isValid) {
        return
    }

    loading.value = true;

    const { data } = await signIn(form);

    loading.value = false;

    if (!data?.success) {
        toast.fire({
            icon: 'error',
            title: data.message,
        });

        form.password = '';
        return;
    }

    auth.setAuthentication({
        access: data.access,
        refresh: data.refresh,
    });
    router.push({ name: 'account' });
}

onMounted(() => {
    if (auth.isAuthenticated) {
        router.push('/account');
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
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

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
                <div v-if="v$.password.$error" class="invalid-feedback">{{ v$.password.$errors[0].$message }}</div>
            </div>

            <div class="form-check text-start mb-3">
                <input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault">
                <label class="form-check-label" for="flexCheckDefault">
                    Remember me
                </label>
            </div>

            <ButtonLoading
                type="submit"
                title="Sign In"
                classes="w-full"
                :loading="loading" />
        </form>

        <div class="py-3 text-center">
            Don't have an account? <RouterLink to="/auth/sign-up">Sign Up</RouterLink>
        </div>
    </div>
</template>
