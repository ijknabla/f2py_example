
subroutine range_iarray(iarray)
  implicit none
  
  integer,intent(inout) :: iarray(:)
  integer :: i
  
  do i = lbound(iarray,1),ubound(iarray,1)
     iarray(i) = i
  end do
  
end subroutine range_iarray
  
