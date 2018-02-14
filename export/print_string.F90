
subroutine print_string(str)
  implicit none
  character(*),intent(in) :: str
  print *, "'" // str // "'"
end subroutine print_string
