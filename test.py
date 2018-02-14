#!/usr/bin/env python3
# -* coding: utf-8 -*-

#f2pyはnumpyの付属プログラムなので、numpy.ndarrayの使用を推奨する。
import numpy

#実装は下記関数名に対応する.F90ファイルを読むこと、
from f2py_example import\
    hello_world, print_integer, print_string, print_iarray, \
    range_iarray, doubleme_iarray, struct_vec_rotate

# hello_world
hello_world()

# integer引数の値渡し
# 引数に対して、int[Python]への変換を行うので注意
print_integer(0)
print_integer(0.0)
print_integer("0")




# character引数の値渡し
# integerの場合と同じく、str[Python]への変換を行う。
# 実際に渡されているのはbytesなのかもしれない？
print_string(0)
print_string(0.0)
print_string( "hello, world!")
print_string(b"HELLO, WORLD!")
print_string( "こんにちは、世界".encode("utf-8")) #Linuxで正しく表示されるはず
print_string( "こんにちは、世界".encode("cp932")) #Windowsで正しく表示されるはず




# 配列の値渡し
# 値渡しについては、結局f2pyでコピーが作成されるので、
# int[Python]に変換できるiterableなら、自由に渡せる。
print("配列の値渡し")
print_iarray([0, 1, 2])
print_iarray(100) #numpyではスカラーも0次元のarrayとみなす
print_iarray(numpy.arange(10))
print_iarray(range(5)) #特定の組み込みiteratorもいけるらしい



# 配列の参照渡し
# 参照渡しの場合、配列要素がメモリ上に連続していなければならない。
# そういった制約のために、numpy.ndarrayのみ利用できる。

# 型のサイズkind[Fortran]については、PythonとFortranで合わせる必要がある。
# integer(4) <=> numpy.int16
# integer(8) <=> numpy.int32
# などと自力で対応付けてもよいが、Cの型に合わせるのがよいように思える。
# Fortran| use iso_c_binding, only : c_int
# Fortran| integer(c_int)
#       v.s.
# Python | numpy.intc

print("配列の参照渡し")
arr0 = numpy.zeros(10, dtype=numpy.intc)
range_iarray(arr0)
print_iarray(arr0)



# 配列を返す関数
# numpy.ndarrayで値を返す。

print(
    doubleme_iarray(range(5))
)


# 構造体の参照渡し
# f2pyでは構造体に直接は対応していないので、
# ctypesで作成したC互換なVec[Python]のアドレスを
# long[C]型で取りだしてFortanに渡す。
# Fortranでアドレスからvec_t[Fortran]に変換して利用する。

import ctypes

# Pythonで作成したC互換なデータ型
class Vec(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_double),
        ("y", ctypes.c_double),
        ("z", ctypes.c_double),
    ]
# 下記データ型と対応する。
# C | struct _vec_t {
# C |     double x, y, z;
# C | };

vec = Vec(10, 20, 30)

print(vec.x, vec.y, vec.z)
struct_vec_rotate(ctypes.addressof(vec))
print(vec.x, vec.y, vec.z)
