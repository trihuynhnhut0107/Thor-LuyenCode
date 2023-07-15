a, b = (input().split())
a = int(a)
b = int(b)
i = a
s = 0
while i <= b:
    if i % 2 == 0:
        s += i
    i += 1
print(s)
