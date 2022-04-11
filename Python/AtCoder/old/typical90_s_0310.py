# 区間DP
# もらうDP
# [le, ri)まで見た時の、最小のコスト
def main():
    n = int(input())
    n *= 2
    A = list(map(int, input().split()))
    INF = float('inf')

    DP = [[INF]*(n+1) for _ in range(n+1)]

    for cnt in range(n+1):
        for le in range(n):
            ri = le + cnt
            if ri > n:
                continue
            if cnt == 0:
                # 誰一人として抜けない場合
                DP[le][ri] = 0
                continue
            dp = INF
            # 1. le, ri-1を今回取り除く場合
            cost = abs(A[le]-A[ri-1])
            dp = min(dp, DP[le+1][ri-1] + cost)
            # 2. [le, mid), [mid, ri)に分ける場合
            for mid in range(le, ri):
                dp = min(dp, DP[le][mid] + DP[mid][ri])
            DP[le][ri] = dp
    ans = DP[0][n]
    print(ans)


main()
