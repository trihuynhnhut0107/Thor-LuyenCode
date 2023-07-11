import string
def Count(n, x):
    count = 0
    for i in n:
        if ord(x) == abs(ord(i) - 32) or x == i or ord(x) == abs(ord(i) + 32):
            count += 1
    return count
def main():
    n = input()
    case = int(input())
    for i in range(0, case):
        x = input()
        print(Count(n, x))
if __name__ == "__main__":
    main()