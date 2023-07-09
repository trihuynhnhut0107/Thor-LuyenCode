s=input()
a=list(map(int,s.split()))
t=False
for i in range(10):
    if a[i]==a[10]:
        print(i+1,end=' ')
        t=True
if t==False:
    print(-1)