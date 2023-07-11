import math
t = int(input())

def Tong(n):
    s = float(0)
    for i in range(n,0,-1):
        s = math.sqrt(i+s)
    return s
a = []
for i in range(t):
    n = int(input())
    a.append(Tong(n))
for i in range(t):

    print("%.5f" % a[i])


