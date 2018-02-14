
function doubleme_iarray(src) result(dst)
  implicit none
  integer,intent(in) :: src(:)
  integer            :: dst(size(src))
  dst(:) = src(:)*2
end function doubleme_iarray
