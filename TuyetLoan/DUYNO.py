import string


def DuyenNo(n):
    temp = n
    if temp < 10 and temp >= 0:
        return True
    else:
        last = temp % 10
        temp = temp // 10
        first = 0
        while temp != 0:
            first = temp % 10
            temp = temp // 10
        if last == first:
            return True
        else:
            return False


def main():
    data = []
    while True:
        line = input()
        if line.strip() == "":
            break
        data.append(int(line))

    for number in data:
        if DuyenNo(number):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
