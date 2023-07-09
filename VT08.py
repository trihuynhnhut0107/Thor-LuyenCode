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
