export interface SignUpForm {
  email: string;
  password: string;
  re_password: string;
}

export interface ActivateForm {
  uid: string;
  token: string;
}

export interface SignInForm {
  email: string;
  password: string;
  rememberMe?: boolean;
}

export interface AuthenticationToken {
  access: string;
  refresh: string;
}
