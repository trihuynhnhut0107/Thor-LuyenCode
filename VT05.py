n,x=[int(x) for x in input().split()]
ds=input()
a=list(map(int,ds.split()))
d=0
for i in range (n):
    if a[i]==x:
        d=d+1
print(d)
