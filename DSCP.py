import math
def KtSoChinhPhuong(n):
    if math.sqrt(n) % 1 != 0:
        return False
    return True

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    count = 0
    for i in range(a, b + 1):
        if KtSoChinhPhuong(i):
            count += 1
    print(count)

if __name__ == "__main__":
    main()

