n = int(input())
s = 0
i = 1
dau = 1
element = 1
while i <= 3 * n + 1:
    s += element
    i += 1
    dau *= -1
    element = i * dau
print(s)
