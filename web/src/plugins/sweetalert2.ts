import Swal from "sweetalert2";

export const toast = Swal.mixin({
  toast: true,
  position: "top-end",
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast: any) => {
    toast.onmouseenter = Swal.stopTimer;
    toast.onmouseleave = Swal.resumeTimer;
  },
});

export const confirm = Swal.mixin({
  showCancelButton: true,
  buttonsStyling: false,
  customClass: {
    confirmButton: `btn btn-sm btn-primary px-2 me-1`,
    cancelButton: `btn btn-sm btn-light px-2`,
  },
});

export const confirmDelete = Swal.mixin({
  showCancelButton: true,
  buttonsStyling: false,
  customClass: {
    confirmButton: `btn btn-sm btn-danger px-2 me-1`,
    cancelButton: `btn btn-sm btn-light px-2`,
  },
});
