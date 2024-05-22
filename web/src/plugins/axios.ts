import { useAuthStore } from "@/stores/auth";
import axios from "axios";

axios.interceptors.request.use((config) => {
  const authStore = useAuthStore();

  config.headers.Authorization = authStore.access ? `Bearer ${authStore.access}` : "";

  return config;
});

axios.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    return Promise.reject(error);
  }
);
