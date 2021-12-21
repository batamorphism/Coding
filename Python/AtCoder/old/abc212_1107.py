# DP[day][cur] day日間移動し、現在curにいる状態の組み合わせ数
# DP[day][cur] = sum(DP[day-1][pre]: pre->curの道が存在する)
# DP[0][cur] = 1 if cur == 0 else 0
# DP[k][0]が答え
# 全ての橋が生き残っているとすると
# DP[day][cur] = sum(DP[day-1][*])
# pre->curが壊れているとすると、DP[day][cur] -= DP[day-1][pre]

mod = 998244353


def main():
    node_end, m, day_max = map(int, input().split())
    DP = [[0]*(node_end) for _ in range(day_max+1)]
    broken = [[] for _ in range(node_end)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        broken[u].append(v)
        broken[v].append(u)

    sum_of_day_bef = 1
    DP[0][0] = 1
    for day in range(1, day_max+1):
        sum_of_day = 0
        # 全ての橋が生きているとした場合
        for cur in range(node_end):
            DP[day][cur] = sum_of_day_bef-DP[day-1][cur]  # 移動しないパターンは削除
            DP[day][cur] %= mod
            sum_of_day += sum_of_day_bef-DP[day-1][cur]
            sum_of_day %= mod
        # 壊れている橋の分を除去
        for pre in range(node_end):
            for cur in broken[pre]:
                DP[day][cur] -= DP[day-1][pre]
                DP[day][cur] %= mod
                sum_of_day -= DP[day-1][pre]
                sum_of_day %= mod
        # print(day, sum_of_day)
        sum_of_day_bef = sum_of_day

    print(DP[day_max][0])


main()
