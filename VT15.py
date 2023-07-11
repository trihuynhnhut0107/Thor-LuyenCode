n = input()
arr = input().split()
arr.sort(key = int)
size = len(arr)
biggest1 = int(arr[size-1]) * int(arr[size-2]) * int(arr[size -3])
biggest2 = int(arr[0]) * int(arr[1]) * int(arr[size-1])
if (biggest1 > biggest2):
    print(biggest1)
else:
    print(biggest2)