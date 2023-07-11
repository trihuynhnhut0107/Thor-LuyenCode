

def main():
    n = input()
    a = input().split()
    first = a[0]
    last = a[len(a)-1]
    a.pop(0)
    a.pop(len(a)-1)
    a.sort(key = int)
    print (first, *a, last)

if __name__ == '__main__':
    main()