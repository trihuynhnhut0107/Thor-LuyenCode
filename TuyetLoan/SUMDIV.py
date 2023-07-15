def SUMDIV(n):
    sum = 0
    temp = int(n // 2 + 1)
    for i in range(1, temp):
        if n % i == 0:
            sum += i
    return sum + n


def main():
    cases = int(input())
    for i in range(0, cases):
        n = int(input())
        print(SUMDIV(n))


if __name__ == "__main__":
    main()
