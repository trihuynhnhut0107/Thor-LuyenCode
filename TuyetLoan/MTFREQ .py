from collections import defaultdict

n = int(input())
x = [int(x) for x in input().split()]
arr  = []
for i in x:
    arr.append(i)
dic_arr = defaultdict(int)
for i in arr:
    dic_arr[i] += 1
print(len(dic_arr))
for key, value in dic_arr.items():
    print(key, value)
