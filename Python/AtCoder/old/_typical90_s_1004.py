def main():
    # 区間DP
    # DP[i][j] = A[i:j]を取り除いている状態。そこまで取り除くのにかかるコスト
    # DP[i][i]は誰も取り除けていない
    # DP[0][n]は全員取り除けている
    INF = 10**10

    n = int(input())
    n = n*2
    A = list(map(int, input().split()))
    # DPのため、n_endは1大きい
    n_end = n+1
    DP = [[INF]*(n_end) for _ in range(n_end)]
    for leave in range(n_end):
        # 除外された人数
        for left in range(n_end):
            right = left+leave
            if right >= n_end:
                continue
            if leave == 0:
                DP[left][right] = 0
                continue
            if leave % 2 != 0:
                continue
            cost_l = DP[left+2][right]+abs(A[left]-A[left+1])
            cost_r = DP[left][right-2]+abs(A[right-2]-A[right-1])
            cost_m = DP[left+1][right-1]+abs(A[left]-A[right-1])
            cost = INF
            for sep in range(n_end):
                cost = min(DP[left][sep]+DP[sep][right], cost)
            DP[left][right] = min(cost_l, cost_r, cost_m, cost)

    print(DP[0][n_end-1])


main()
