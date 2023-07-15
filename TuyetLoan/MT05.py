def Swap(m, n):
    return n, m


def main():
    m, n, cot = input().split()
    m = int(m)
    n = int(n)
    cot = int(cot)
    cot -= 1
    arr = []
    count = 0
    x = [int(x) for x in input().split()]
    arr2D = []
    for i in x:
        arr.append(i)
    for i in range(0, m):
        arr2D.append([])
        for j in range(0, n):
            arr2D[i].append(arr[i + j + count])
        count += n - 1
    for i in range(0, m - 1):
        for j in range(1, m):
            if arr2D[i][cot] > arr2D[j][cot]:
                arr2D[i][cot], arr2D[j][cot] = Swap(arr2D[i][cot], arr2D[j][cot])
    for i in range(0, m):
        for j in range(0, n):
            print(arr2D[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()
