def GT(n):
    t = 1
    i = 2
    while i <= n:
        t = t * i
        i += 1
    return t
def main():
    n, k = (input().split())
    n = int(n)
    k = int(k)
    t1 = GT(n)
    t2 = GT(n - k)
    t3 = GT(k)
    result = (int)(t1 / (t2 * t3))
    print(result)
if __name__ == "__main__":
    main()
    