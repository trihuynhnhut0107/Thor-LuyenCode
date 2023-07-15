m, n = input().split()
m = int(m)
n = int(n)
x = [int(x) for x in input().split()]
arr = []
count = 0
for i in x:
    arr.append(i)
for i in range(0, m):
    for j in range(0 + count, n + count):
        print(arr[i + j], end=" ")
    count += n - 1
    print()
