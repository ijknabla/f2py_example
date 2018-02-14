
subroutine struct_vec_rotate(addr)
  use iso_c_binding
  use ptr_util
  implicit none

  type,bind(C) :: vec_t
     real(c_double) :: x, y, z
  end type vec_t
  
  integer(c_long),intent(in) :: addr
  type(vec_t),pointer        :: vec_p
  real(c_double) :: temp

  call c_f_pointer(l2p(addr), vec_p)
  temp = vec_p%x
  vec_p%x = vec_p%y
  vec_p%y = vec_p%z
  vec_p%z = temp
  
end subroutine struct_vec_rotate
