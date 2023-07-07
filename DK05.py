import math

n = int(input())
if n >= 0 and math.sqrt(n) == float(int(math.sqrt(n))):
    print('YES')
else:
    print ('NO')