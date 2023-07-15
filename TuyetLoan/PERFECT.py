n = int(input())
arr = []
x = [int(x) for x in input().split()]
for i in x:
    arr.append(i)
minValue = []
for i in range(0, n - 1):
    for j in range(1, n):
        if i != j:
            value = abs(arr[i] - arr[j])
            minValue.append(value)
min = 100000000
for i in minValue:
    if i < min:
        min = i
print(min)