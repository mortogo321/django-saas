export function singleView(unMounted: boolean = false) {
  const main = document.querySelector("main");
  const styles = ["d-flex", "justify-content-center", "align-items-center"];

  if (main) {
    if (unMounted) {
      main.classList.remove(...styles);
    } else {
      main.classList.add(...styles);
    }
  }
}

export function errorHandler(error: any) {
  const message = error.response?.data?.message || error.response?.data?.detail || error.response?.statusText || error;

  return {
    data: {
      success: false,
      message,
    },
  };
}
