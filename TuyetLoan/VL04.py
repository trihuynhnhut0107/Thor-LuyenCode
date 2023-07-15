a = int(input())
i = 2
s = 0
while i <= a:
    s = (float)("{0:.{1}f}".format(s + 1 / i, 4))
    i += 1
print(s)
