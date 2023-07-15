def Is_Prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
def main():
    n = int(input())
    for i in range(0, n):
        a, b = input().split()
        a = int(a)
        b = int(b)
        count = 0
        for j in range(a, b + 1):
            if Is_Prime(j):
                count += 1
        print(count)
if __name__ == "__main__":
    main()
