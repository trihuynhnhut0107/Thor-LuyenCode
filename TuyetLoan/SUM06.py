import math
def SUM06(n):
    s = 0
    i = 1
    while i <= n:
        s += math.sqrt(2 + s)
        i += 1
    s = "{:.5f}".format(s)
    return s
def main():
    case = int(input())
    for i in range(0, case):
        n = int(input())
        print(SUM06(n))
if __name__ == "__main__":
    main()
