b, c = [int(x) for x in input().split()]
if b == 0:
    if c == 0:
        print ('WOW')
    else:
        print ('NO')
else:
    print ("{0:.2f}".format(-c / b))