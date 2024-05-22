import type { SignInForm, SignUpForm } from "@/types/auth";
import { errorHandler } from "@/utils";
import axios from "axios";

export const apiUrl = import.meta.env.VITE_API_URL;

export async function signUp(form: SignUpForm) {
  const url = `${apiUrl}/auth/users/`;

  return await axios.post(url, form);
}

export async function signIn(form: SignInForm) {
  try {
    const url = `${apiUrl}/auth/jwt/create/`;

    return await axios.post(url, form);
  } catch (error) {
    return errorHandler(error);
  }
}
