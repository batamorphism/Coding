# 巡回セールスマン
def main():
    node_end = int(input())
    node_list = [tuple(map(int, input().split())) for _ in range(node_end)]

    nbh_of = [[] for _ in range(node_end)]
    for fr in range(node_end):
        for to in range(node_end):
            fr_x, fr_y, fr_z = node_list[fr]
            to_x, to_y, to_z = node_list[to]
            cost = abs(to_x - fr_x) + abs(to_y - fr_y) + max(0, to_z - fr_z)
            nbh_of[fr].append((to, cost))

    # 巡回セールスマン
    ALL = 1 << node_end
    INF = float('inf')
    DP = [[INF]*node_end for _ in range(ALL)]
    # DP[S][cur]  既にSを探索し、現在curにいるときの最小コスト
    DP[0][0] = 0
    # 配るDP
    for cur_S in range(ALL):
        for cur_node in range(node_end):
            cur_cost = DP[cur_S][cur_node]
            for nex_node, cost in nbh_of[cur_node]:
                nex_S = cur_S | (1 << nex_node)
                nex_cost = cur_cost + cost
                DP[nex_S][nex_node] = min(DP[nex_S][nex_node], nex_cost)

    ans = DP[ALL-1][0]
    print(ans)


main()
