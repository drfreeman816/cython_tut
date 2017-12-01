# Dynamic typed variables (Python):
#
# x = 5
#
# x = 'gary'
#
# Static typed variables (C/C++):
#
# int x = 5;
#
# x = 'gary'; // Error


cpdef int test(int x):
    cdef int y = 0
    cdef int i
    for i in range(x):
        y += i
    return y
