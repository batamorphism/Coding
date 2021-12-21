# 区間DP
def main():
    INF = float('inf')
    n = int(input())
    n_end = n*2+1
    A = list(map(int, input().split()))

    # DP[le][ri] = [le, ri)の最大値
    # DP[i][i] = 0
    # DP[0][n_end-1] = 答え
    # DP[le][ri] = DP[le+1][ri-1] + abs(A[le]-A[ri-1])
    DP = [[INF]*n_end for _ in range(n_end)]
    for d_i in range(n_end):
        for le in range(n_end-1):
            if d_i == 0:
                DP[le][le] = 0
                continue
            ri = le + d_i
            if ri >= n_end:
                break
            dp1 = INF
            if ri-1 > le:
                dp1 = DP[le+1][ri-1] + abs(A[le]-A[ri-1])
            dp2 = INF
            for sep in range(le, ri+1):
                dp2 = min(dp2, DP[le][sep] + DP[sep][ri])
            DP[le][ri] = min(dp1, dp2)
    print(DP[0][n_end-1])


main()
