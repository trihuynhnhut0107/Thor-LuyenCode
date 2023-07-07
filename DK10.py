m, y = [int(x) for x in input().split()]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if ( y % 4 == 0 and y % 100 != 0):
    days[1] += 1
if m <= 0 or m > 12 or y <= 0 or y > 100000:
    print('INVALID')
else:
    print(days[m - 1])