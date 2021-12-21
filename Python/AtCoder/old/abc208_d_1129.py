from copy import deepcopy
# ワーシャルフロイド法
INF = 10**6*400+1


def main():
    n, m = map(int, input().split())
    # 隣接行列形式
    A = [[INF] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        A[a][b] = c

    DP = deepcopy(A)
    ans = 0
    for k in range(n):
        for fr in range(n):
            for to in range(n):
                # dp1 = A[fr][to]
                dp2 = DP[fr][k]+DP[k][to]
                dp3 = DP[fr][to]
                dp = min(dp2, dp3)
                if dp == INF or fr == to:
                    pass
                else:
                    ans += dp
                DP[fr][to] = dp

    print(ans)


main()
