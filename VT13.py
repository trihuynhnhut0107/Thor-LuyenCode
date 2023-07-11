n = input()
a = input().split()

lc = int(a[0])+int(a[len(a)-1])
lc1, lc2 = len(a)-1,0

for i in range(len(a)-1):
    if (int(a[i])+int(a[i+1])>= lc):
        lc1,lc2 = i, i+1
        lc = int(a[i])+int(a[i+1])

print(a[lc1],a[lc2])

