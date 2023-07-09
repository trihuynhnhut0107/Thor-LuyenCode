def max(a,n):
    max=0
    for i in range(1,n):
        if a[max]<=a[i]:  
            max=i
    return max
if __name__=="__main__":
    n=int(input())
    ds=input()
    a=list(map(int,ds.split()))
    print(max(a,n))

