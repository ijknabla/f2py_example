
#ifdef  __cplusplus
extern "C" {
#endif /* __cplusplus */

  long p2l(void* p){
    return (long) p ;
  }

  void* l2p(long i){
    return (void*) i ;
  }
  
#ifdef  __cplusplus
}
#endif /* __cplusplus */
