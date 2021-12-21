# mが小さいことをうまく使う
# nの完全グラフのうち、mに入っているものが使えない
# n = 5000と小さい、n**2くらいならいける？
# DP[day]][node] day日目まで見たときの、最後にnodeにいる状態での組み合わせ数
# DP[0][0] = 1, DP[0][*] = 0 最初はnode0にいる
# DP[day][node] = SUM(DP[day-1]) - SUM(DP[day-1][m[node]]) - DP[day-1][node]
mod = 998244353


def main():
    n, m, k = map(int, input().split())
    bad_of = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        bad_of[u].append(v)
        bad_of[v].append(u)

    DP = [[0] * n for _ in range(k + 1)]
    DP[0][0] = 1

    for day in range(1, k+1):
        sum_dp_bef_day = sum(DP[day-1])
        sum_dp_bef_day %= mod
        for node in range(n):
            dp = sum_dp_bef_day  # SUM(DP[day-1])
            for bad in bad_of[node]:
                dp -= DP[day-1][bad]
            dp -= DP[day-1][node]
            dp %= mod
            DP[day][node] = dp

    ans = DP[k][0]
    print(ans)


main()
