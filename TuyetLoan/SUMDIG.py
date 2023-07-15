def Sum(n):
    temp = n
    sum = 0
    while temp != 0:
        sum += temp % 10
        temp = temp // 10
    print(sum)


def main():
    cases = int(input())
    for i in range(0, cases):
        n = int(input())
        Sum(n)


if __name__ == "__main__":
    main()
