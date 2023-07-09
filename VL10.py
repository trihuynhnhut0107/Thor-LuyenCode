def KiemTraNguyenTo(n):
    if n <= 1:
        print("NO")
    elif n == 2:
        print("YES")
    else:
        for i in range(3, n - 1):
            if n % i == 0:
                print("NO")
                return
        print("YES")
def main():
    n = int(input())
    KiemTraNguyenTo(n)
if __name__ == "__main__":
    main()