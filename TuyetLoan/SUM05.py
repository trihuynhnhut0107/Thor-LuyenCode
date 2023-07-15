def SUM05(n):
    sum = 0
    for i in range(1, n + 1):
        sum += 1 / i
    sum = "{:.5f}".format(sum)
    print(sum)


def main():
    case = int(input())
    for i in range(0, case):
        n = int(input())
        SUM05(n)


if __name__ == "__main__":
    main()
