def INVSUM(n):
    sum = 1
    i = 3
    while i <= 2 * n - 1:
        sum += 1 / i
        i += 2
    sum = sum = "{:.5f}".format(sum)
    return sum
def main():
    case = int(input())
    for i in range (0, case):
        n = int(input())
        print(INVSUM(n))
if __name__ == "__main__":
    main()
