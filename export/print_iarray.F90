
subroutine print_iarray(iarray)
  use iso_c_binding
  implicit none
  integer(c_int),intent(in) :: iarray(:)
  print *, "size =", size(iarray)
  print *, iarray
end subroutine print_iarray
