def max(a,n):
    max=0
    for i in range(1,n):
        if a[max]<a[i]:  
            max=i
    return max
if __name__=="__main__":
    n=int(input())
    ds=input()
    a=list(map(int,ds.split()))
    m= a[max(a,n)]
    while len(a)!=0 and m==a[max(a,n)]:
        a.remove(m)
        n=n-1
    if not a:
        print('NOT FOUND')
    else:
        print(a[max(a,n)])
