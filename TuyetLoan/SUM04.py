def SUM04(n):
    deno = 0
    i = 1
    sum = 0
    for i in range(1, n + 1):
        deno += i
        sum += 1 / deno
    return round(sum, 8)


def main():
    case = int(input())
    for i in range(0, case):
        n = int(input())
        if n == 1:
            print("1.00000000")
        elif n == 0:
            print("")
        else:
            print(SUM04(n))


if __name__ == "__main__":
    main()
