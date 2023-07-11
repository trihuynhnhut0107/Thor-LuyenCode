import math

a = int(input())
dt = a * a * math.pi
kq = round(dt/2, 3)
kq = f'{kq:.3f}'
print(kq)