n = int(input())
arr = []
x = [int(x) for x in input().split()]
for i in x:
    arr.append(i)
sum = 0
for i in range(1, n, 2):
    sum += arr[i]
print(sum)
