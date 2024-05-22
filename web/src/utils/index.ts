export function errorHandler(error: any) {
  const message = error.response?.data?.message || error.response?.data?.detail || error.response?.statusText || error;

  return {
    data: {
      success: false,
      message,
    },
  };
}
