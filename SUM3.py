n = int(input())
s = int(0)
for i in range(1,n+1):
    s = s + 1/(i*(i+1))

s = f'{s:.5f}'
print(s)
