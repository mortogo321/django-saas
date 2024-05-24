<script setup lang="ts">
defineProps({
    type: {
        type: String as () => "submit" | "button",
        default: 'button',
    },
    classes: {
        type: String,
        default: '',
    },
    title: {
        type: String,
        default: 'Submit',
    },
    loading: Boolean,
})
</script>

<template>
    <button
        :type="type"
        :class="[{ 'justify-content-between': loading, 'justify-content-center': !loading }, classes]"
        class="btn btn-primary py-2 d-flex align-items-center gap-1">
        <span v-if="loading" class="spinner-border spinner-border-sm" aria-hidden="true"></span>
        <span role="status">{{ title }}</span>
        <span v-if="loading"></span>
    </button>
</template>
