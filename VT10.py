
n=int(input())
ds=input()
a=list(map(int,ds.split()))
for i in range(n-1):
    for j in range(i+1,n):
        if a[j]>a[i]:
            a[j],a[i]=a[i],a[j]
for i in range(len(a)):
    print(a[i],end=' ')