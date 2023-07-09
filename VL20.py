a,b=[str(x) for x in input().split()]
for ch in range(ord(a), ord(b)+1):
    if (ch>=97):
        print(chr(ch-32),end=' ')
    else:
        print(chr(ch),end=' ')
