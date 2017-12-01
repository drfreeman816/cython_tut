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


def test(x):
    y = 0
    for i in range(x):
        y += i
    return y
