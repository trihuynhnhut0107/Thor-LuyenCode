def RANGED(a, b, c, d):
    if a >= c and b <= d and b >= a:
        return True
    elif a <= c and b <= d and c <= b:
        return True
    elif a <= c and b >= d and a <= d:
        return True
    elif a >= c and a <= d and d <= b:
        return True
    else:
        return False


def main():
    a, b, c, d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if RANGED(a, b, c, d):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
