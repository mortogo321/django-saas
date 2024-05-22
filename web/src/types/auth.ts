export interface SignUpForm {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
}

export interface SignInForm {
  email: string;
  password: string;
  rememberMe?: boolean;
}
