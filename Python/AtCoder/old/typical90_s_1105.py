# 区間DP
# DP[le][ri] = [le, ri)が抜けている状態でのコストの最小値
# DP[le][ri] = min(DP[le][sep]+DP[sel][ri], cost[le][ri]+DP[le+1][ri-1])
# O(N**3)なので間に合う

INF = 10**9


def main():
    n = int(input())
    n *= 2
    A = list(map(int, input().split()))

    DP = [[INF] * (n+1) for _ in range(n+1)]

    def cost(le, ri):
        # leとri-1が抜けるときのコスト
        if ri <= le:
            return INF
        return abs(A[le] - A[ri - 1])

    for delta in range(n+1):  # 抜けた人数
        for le in range(n):
            ri = le + delta
            if ri > n:
                break
            if delta == 0:
                DP[le][ri] = 0
                continue
            dp = INF
            for sep in range(le, ri+1):
                dp = min(DP[le][sep] + DP[sep][ri], dp)
            dp = min(DP[le+1][ri-1] + cost(le, ri), dp)
            DP[le][ri] = dp

    print(DP[0][n])


main()
