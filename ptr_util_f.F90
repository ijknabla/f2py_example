
module ptr_util
  
  use iso_c_binding
  implicit none
  
  interface
     function l2p(l) result(p) bind(C)
       import c_long, c_ptr
       implicit none
       integer(c_long),value :: l
       type(c_ptr)          :: p
     end function l2p
     
     function p2l(p) result(l) bind(C)
       import c_long, c_ptr
       implicit none
       type(c_ptr),value    :: p
       integer(c_long)       :: l
     end function p2l
  end interface
  
end module ptr_util
