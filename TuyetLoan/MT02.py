m, n = input().split()
m = int(m)
n = int(n)
x = [int(x) for x in input().split()]
arr = []
arr2D = []
count = 0
for i in x:
    arr.append(i)
for i in range(0, m):
    arr2D.append([])
    for j in range(0, n):
        arr2D[i].append(arr[i + j + count])
        # print(arr[i + j ], end = ' ')
    count += n - 1
sum = 0
for i in range(0, m):
    for j in range(0, n):
        if i % 2 != 0:
            sum += arr2D[i][j]
print(sum)
