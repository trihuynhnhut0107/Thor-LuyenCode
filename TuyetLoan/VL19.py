a, b = (input().split())
a = int(a)
b = int(b)
count = 0
b = b - 1
a = a + 1
while b >= a:
    if b % 3 == 0:
        count += 1
        print(b, end = ' ')
    b -= 1
if count == 0:
    print("NOT FOUND")
