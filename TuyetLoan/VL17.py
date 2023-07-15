def SoLuongUocSo(a):
    count = 0
    for i in range (1, a + 1):
        if a % i == 0:
            count += 1
    return count;
def main():
    n = int(input())
    print(SoLuongUocSo(n))
if __name__ == "__main__":
    main()