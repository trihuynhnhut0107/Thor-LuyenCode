n = input()
arr = input().split()
arr.sort(key = int)
size = len(arr)
begin = int(arr[0])*int(arr[1])
end = int(arr[size-1])*int(arr[size-2])
if (begin > end):
    print(begin)
else:
    print(end)