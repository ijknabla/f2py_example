
PROJECT_NAME := f2py_example
PYLIB_SUFFIX := .cpython-35m-x86_64-linux-gnu.so
TEST         := test.py

PYLIB := ${PROJECT_NAME}${PYLIB_SUFFIX}

SRCS := $(wildcard export/*.[fF]90)

.PHONEY: all
all: ${PYLIB}

#ptrUtil_f.o ptrUtil.o

ptr_util_f.o: ptr_util_f.F90
	gfortran -o $@ -c $^

ptr_util.o: ptr_util.c
	gcc -o $@ -c $^

${PYLIB}: ${SRCS} ptr_util.o ptr_util_f.o
	f2py -m ${PROJECT_NAME} -c $^

.PHONEY: test
test: ${PYLIB}
	./${TEST}

.PHONEY: clean
clean:
	rm -rf *.so *.o *.mod
