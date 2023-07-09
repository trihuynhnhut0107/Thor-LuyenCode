n,x=[int(x) for x in input().split()]
ds=input()
a=list(map(int,ds.split()))
t=False
for i in range (n):
    if a[i]==x:
        t=True
        print('YES')
        break
if t==False:
    print('NO')
