x, n = input().split()
x = int(x)
n = int(n)
t = x
s = x
i = 2
GT = 1
while i <= n:
    t *= x
    GT *= i
    s = (float)('{0:.{1}f}'.format(s + (t / GT), 2))
    i += 1
print(s)
