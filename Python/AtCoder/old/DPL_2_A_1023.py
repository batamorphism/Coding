INF = 10**9


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        s, t, d = map(int, input().split())
        nei_of[s].append((d, t))

    ALL = 1 << node_end
    # DP[node][bit] : 現在nodeにいて、bit上の全nodeを探索するのにかかる最大のコスト
    # 答えは、DP[0][ALL-1]になる
    DP = [[-1]*ALL for _ in range(node_end)]

    # bitDPはメモ化再帰
    def dfs(pre_node, pre_bit):
        if DP[pre_node][pre_bit] != -1:
            return DP[pre_node][pre_bit]
        if pre_bit == 0 and pre_node == 0:
            return 0
        ret = INF
        for d, cur_node in nei_of[pre_node]:
            if not(pre_bit >> cur_node & 1):
                continue
            cur_bit = pre_bit ^ 1 << cur_node
            pre_d = dfs(cur_node, cur_bit)
            ret = min(d+pre_d, ret)
        DP[pre_node][pre_bit] = ret
        return ret

    ans = dfs(0, ALL-1)
    if ans == INF:
        ans = -1
    print(ans)


main()
