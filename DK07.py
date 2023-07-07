import math

a, b, c = [float(x) for x in input().split()]
if a == 0:
    if b == 0:
        if c == 0:
            print ('WOW')
        else:
            print ('NO')
    else:
        print ("{0:.2f}".format(-c / b))
else:
    denta = b * b - 4 * a * c
    if denta < 0:
        print ('NO')
    elif denta == 0:
        print("{0:.2f}".format(-b / (2 * a)))
    else:
        denta = math.sqrt(denta)
        x1 = (-b + denta) / (2 * a)
        x2 = (-b - denta) / (2 * a)
        print ("{0:.2f}".format(x2), "{0:.2f}".format(x1))