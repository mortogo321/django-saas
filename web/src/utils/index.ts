export function errorHandler(error: any) {
  let message = error.response?.data?.message || error.response?.data?.detail || error.response?.statusText || error;

  if (error.response?.status === 400) {
    const values = Object.values(error.response.data).pop() as string[];

    message = values[0];
  }

  return {
    data: {
      success: false,
      message,
    },
  };
}
