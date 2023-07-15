arr = []
n = int(input())
x = [int(x) for x in input().split()]
for i in x:
    arr.append(i)
sum = 0
for i in arr:
    sum += i
print(sum, end=" ")
count = 0
for i in arr:
    if i % 2 == 0:
        count += 1
print(count, end=" ")
flag = 0
for i in range(len(arr) - 1, 0, -1):
    if arr[i] > 0:
        print(arr[i])
        break
