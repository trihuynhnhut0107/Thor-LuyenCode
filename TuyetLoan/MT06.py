import math
def KtSoChinhPhuong(n):
    if math.sqrt(n) % 1 != 0:
        return False
    return True

def main():
    m,n = input().split()
    m = int(m)
    n = int(n)
    arr = []
    for i in range(0, m):
        arr.append([])
        x = [int(x) for x in input().split()]
        for j in x:
            arr[i].append(j)
    lessValue = set()
    for i in range(0, m):
        for j in range(0, n):
            if KtSoChinhPhuong(arr[i][j]):
                lessValue.add(arr[i][j])
    arrArrange = []
    for i in lessValue:
        arrArrange.append(i)
    arrArrange.sort()
    for i in arrArrange:
        print(i, end = ' ')
if __name__ == "__main__":
    main()
