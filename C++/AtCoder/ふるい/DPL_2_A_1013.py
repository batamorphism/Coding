import sys
sys.setrecursionlimit(10**9)

INF = 10**9


def main():
    node_end, edge_end = map(int, input().split())
    ALL = 1 << node_end
    nei_of = [[] for _ in range(edge_end+1)]
    for _ in range(edge_end):
        fr, to, di = map(int, input().split())
        nei_of[fr].append((to, di))
        # nei_of[to].append((fr, di))

    memo = [[-1]*node_end for _ in range(ALL)]

    def dfs(pre_bit, pre_node):
        # 0から出発して、pre_bitを通過して、現在pre_nodeにいる状態での最短経路
        pre_d = memo[pre_bit][pre_node]
        if pre_d != -1:
            return pre_d
        if pre_bit == 0 and pre_node == 0:
            # 初期値
            return 0
        if pre_bit == 0:
            return INF
        ret = INF
        for cur_node, di in nei_of[pre_node]:
            if (pre_bit >> cur_node & 1) == 0:
                continue
            cur_bit = pre_bit ^ (1 << cur_node)
            cur_d = dfs(cur_bit, cur_node)+di
            ret = min(cur_d, ret)
        memo[pre_bit][pre_node] = ret
        return ret

    ans = dfs(ALL-1, 0)
    if ans == INF:
        print(-1)
    else:
        print(ans)


main()
