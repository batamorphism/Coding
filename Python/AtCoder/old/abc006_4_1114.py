INF = 10**9


def main():
    n = int(input())
    C = [int(input()) for _ in range(n)]

    # Cの最長部分増加列を求める
    DP = [INF]*n
    # DP[i] = C[i]の最長部分増加列の長さ
    # DP[i] > C[i]かつDP[i-1] <= C[i]となる最大のiを求める
    # これは、DP[i] > C[i]となる最小のiを求めればよい
    # これは、bisect_rightをすればよい
    lis_len = 0
    for c in C:
        lo = 0
        hi = n
        while lo < hi:
            mid = (lo + hi)//2
            if c < DP[mid]:
                hi = mid
            else:
                lo = mid + 1
        DP[lo] = c
        lis_len = max(lis_len, lo+1)
        # print(c, lo, DP[lo], DP)

    print(n-lis_len)


main()
