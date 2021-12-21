INF = 10**9


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to, d = map(int, input().split())
        nei_of[fr].append((d, to))

    ALL = 1 << node_end
    memo = [[-1]*node_end for _ in range(ALL)]

    def dfs(pre_bit, pre_node):
        # 現在、pre_bitを探索済みで、pre_nodeにいる状態で
        # 残りを全部探索するのにかかる最小距離
        m = memo[pre_bit][pre_node]
        if m != -1:
            return m
        ret = INF
        if pre_bit == ALL-1 and pre_node == 0:
            return 0
        for d, cur_node in nei_of[pre_node]:
            if pre_bit >> cur_node & 1:
                # 既に探索済み
                continue
            cur_bit = pre_bit ^ (1 << cur_node)
            cur_d = dfs(cur_bit, cur_node)
            cur_d += d
            ret = min(cur_d, ret)
        memo[pre_bit][pre_node] = ret
        return ret

    ans = dfs(0, 0)
    if ans == INF:
        print(-1)
    else:
        print(ans)


main()
