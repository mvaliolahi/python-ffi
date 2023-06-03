from cffi import FFI
ffibuilder = FFI()
ffibuilder.cdef("int add(int a, int b);")
ffibuilder.set_source("padd",'#include "add.h"',sources=["add.c"])
ffibuilder.compile()
