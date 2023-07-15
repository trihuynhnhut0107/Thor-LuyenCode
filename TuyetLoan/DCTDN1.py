def longest(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def main():
    n = int(input())
    arr = []
    x = [int(x) for x in input().split()]
    for i in x:
        arr.append(i)
    print(longest(arr))


if __name__ == "__main__":
    main()
