n = int(input())
s = 1
if n < 0:
    print("NO")
elif n == 0:
    print("NO")
else:
    for i in range(2, n - 1):
        if n % i == 0:
            s += i
    if s == n:
        print("YES")
    else:
        print("NO")
