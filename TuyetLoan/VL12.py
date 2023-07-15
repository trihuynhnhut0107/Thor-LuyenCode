import math

n = int(input())
if n == 0:
    print("INF")
else:
    n = math.fabs(n)
    n = int(n)
    i = n
    while i > 0:
        if n % i == 0:
            print(i, end=" ")
        i = i - 1
