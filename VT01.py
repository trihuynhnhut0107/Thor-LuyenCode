n=int(input())
ds=input()
a=list(map(int,ds.split()))
max=a[0]
for i in range(1,n):
    if max<a[i]:  
        max=a[i]
print(max)
