def ktNguyenTo(n):
    t=True
    if (n<=1):
        t=False
    else:
        i=2
        while(i*i<=n):
            if n%i==0:
                t=False
                break
            i=i+1
    return t
if __name__=="__main__":
    n=int(input())
    ds=input()
    a=list(map(int,ds.split()))
    b=[]
    for i in range(n):
        if ktNguyenTo(a[i])==True:
            b.append(a[i])
    b=set(b)
    b=list(b)
    b.sort()
    for i in range(len(b)):
        print(b[i],end=' ')