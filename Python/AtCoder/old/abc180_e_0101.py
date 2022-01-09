# DP[bit][i] 現在iにいて、bitを探索済みの状態にするための最小コスト
# DP[pre_bit][i] -> DP[pre_bit][i]+cost(i, j)
def main():
    n_end = int(input())
    INF = float('inf')
    ALL = 1 << n_end
    DP = [[INF]*n_end for _ in range(ALL)]
    cost_of = [[INF]*n_end for _ in range(n_end)]

    point_list = [tuple(map(int, input().split())) for _ in range(n_end)]

    for i, p_i in enumerate(point_list):
        for j, p_j in enumerate(point_list):
            if i == j:
                continue
            a, b, c = p_i
            p, q, r = p_j
            cost = abs(p-a)+abs(q-b)+max(r-c, 0)
            cost_of[i][j] = cost

    DP[0][0] = 0
    # 2**17*17*17 = 37879808
    for pre_bit in range(ALL):
        for i in range(n_end):
            for j in range(n_end):
                cur_bit = pre_bit | (1 << j)
                dp = DP[pre_bit][i] + cost_of[i][j]
                DP[cur_bit][j] = min(DP[cur_bit][j], dp)

    ans = DP[ALL-1][0]
    print(ans)


main()
