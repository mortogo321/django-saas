import { defineStore } from "pinia";

export interface AuthenticationToken {
  access: string;
  refresh: string;
}

export const useAuthStore = defineStore({
  id: "auth",
  state: () => ({
    access: "",
    refresh: "",
  }),
  getters: {
    isAuthenticated: (state) => !!state.access,
  },
  actions: {
    setAuthentication(token: AuthenticationToken) {
      this.access = token.access;
      this.refresh = token.refresh;
    },
  },
});
