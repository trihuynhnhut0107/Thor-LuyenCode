import math

a, b = input().split()
a = int(a)
b = int(b)
a = abs(a)
b = abs(b)
while a != 0 and b != 0:
    if a > b:
        a = a - b
    else:
        b = b - a
if a != 0:
    print(a)
else:
    print(b)
