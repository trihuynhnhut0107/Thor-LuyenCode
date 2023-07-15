import math

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a + b) > c and (b + c) > a and (a + c) > b:
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    area = "{:.2f}".format(area)
    print((a + b + c), area)
else:
    print("NO")
