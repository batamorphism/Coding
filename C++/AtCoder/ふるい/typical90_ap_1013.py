mod = 10**9+7


def main():
    k = int(input())
    # DP[sum] = 合計値がsumとなる数の個数
    DP = [0]*(k+1)
    for sum in range(k+1):
        if sum <= 1:
            DP[sum] = 1
            continue
        for d_sum in range(1, 10):
            if sum-d_sum < 0:
                break
            DP[sum] += DP[sum-d_sum]
            DP[sum] %= mod

    ans = 0
    if k % 9 == 0:
        ans = DP[k]
    print(ans)


main()
