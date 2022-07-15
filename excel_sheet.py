import string
from numpy import character
def tostring(n):
    return (chr(n+64))
a = 2
b = a//26
c = 0
s = ''
if a >= 1 and a <= 26:
    print(tostring(a))
else:
    while a > 26:
        c = a%26
        if c == 0:
            b = b-1
            s = s+tostring(b)
            s = s+tostring(1*26)
            print(s)
        else:
            s = tostring(c) + s
        a = a//26
    if c != 0:
        s = tostring(a)+s
    print(s)