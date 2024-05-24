<script setup lang="ts">
import { useVuelidate } from '@vuelidate/core';
import { email, minLength, required, sameAs } from '@vuelidate/validators';
import { computed, nextTick, onMounted, reactive, ref } from 'vue';

import logo from '@/assets/logo.svg';
import ButtonLoading from '@/components/ButtonLoading.vue';
import { toast } from '@/plugins/sweetalert2';
import { signUp } from '@/services/auth';
import { useAuthStore } from '@/stores/auth';
import { useRouter } from 'vue-router';

const auth = useAuthStore();
const router = useRouter();
const autoFocus = ref();
const form = reactive({
    email: '',
    password: '',
    re_password: '',
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
        re_password: {
            required,
            sameAs: sameAs(form.password),
        },
    }
})
const v$ = useVuelidate(rules, form)
const loading = ref(false)

async function onSubmit() {
    const isValid = await v$.value.$validate()

    if (!isValid) {
        return
    }

    loading.value = true;

    const { data } = await signUp(form);

    loading.value = false;

    if (!data?.success) {
        toast.fire({
            icon: 'error',
            title: data.message,
        });

        form.password = '';
        form.re_password = '';
        return;
    }

    router.push('/auth/sign-up/success');
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
                <div v-if="v$.password.$error" class="invalid-feedback">{{ v$.password.$errors[0].$message }}</div>
            </div>

            <div class="form-floating mb-3">
                <input
                    type="password"
                    class="form-control"
                    :class="{ 'is-invalid': v$.re_password.$error }"
                    placeholder="Confirm Password"
                    v-model="form.re_password">
                <label>Confirm Password</label>
                <div v-if="v$.re_password.$error" class="invalid-feedback">{{ v$.re_password.$errors[0].$message }}</div>
            </div>

            <ButtonLoading
                type="submit"
                title="Sign Up"
                classes="w-full"
                :loading="loading" />
        </form>

        <div class="py-3 d-flex flex-wrap justify-content-center align-items-center gap-1">
            Already have an account? <RouterLink to="/auth/sign-in">Sign In</RouterLink>
            <span class="divider"></span>
            Forget your password? <RouterLink to="/">Reset Password</RouterLink>
        </div>
    </div>
</template>
