import math
a,b = (input().split())
a = float(a)
b = float(b)
if a % 1 != 0 or b % 1 != 0:
    print("INVALID")
else:
    a = int(a)
    b = int(b)
    if b == 0:
        print("INVALID")
    elif a == 0:
        print(a)
    elif b == 1:
        print (a)
    else:
        tempA = abs(a)
        tempB = abs(b)
        while tempA != 0 and tempB != 0:
            if tempA > tempB:
                tempA = tempA - tempB
            else:
                tempB = tempB - tempA
        if tempA != 0:
            a = a / tempA
            b = b / tempA
        else:
            a = a / tempB
            b = b / tempB
        if b < 0:
            a = a * (-1)
            b = abs(b)
        a = int(a)
        b = int(b)
        print (a, b)

