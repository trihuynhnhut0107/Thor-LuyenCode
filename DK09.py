y = int(input())

if y <= 0 or y > 100000:
    print('INVALID')
elif (y % 4 == 0 and y % 100 != 0):
    print('YES')
else:
    print('NO')