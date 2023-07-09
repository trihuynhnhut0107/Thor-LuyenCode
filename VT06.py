def Tongle(a,n):
    s=0
    d=0
    for i in range(n):
        if a[i]%2!=0:
            s=s+a[i]
            d=d+1
    return s,d
if __name__=="__main__":
    n=int(input())
    ds=input()
    a=list(map(int,ds.split()))
    s,d=Tongle(a,n)
    print("{:.4f}".format(s/d))

