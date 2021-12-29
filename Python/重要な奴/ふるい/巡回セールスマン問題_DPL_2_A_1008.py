def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        s, t, d = map(int, input().split())
        nei_of[s].append((t, d))
        # nei_of[t].append((s, d)) Directedなので逆向きはなし
    # bitDP
    # DP[bit][to_node]
    # bitに訪問済みで現在to_nodeにいる状態での
    # 残りALL^bitを探索するのにかかる距離
    ALL = 1 << node_end
    INF = 10**9
    DP = [[-1]*node_end for _ in range(ALL)]

    def dfs(pre_bit, pre_node, DP):
        if DP[pre_bit][pre_node] != -1:
            # 既に訪問済みである
            return DP[pre_bit][pre_node]
        if pre_bit == ALL-1 and pre_node == 0:
            # 停止処理
            # 全ての頂点に探索済みかつ現在頂点0にいる
            return 0

        ret = INF
        for cur_node, d in nei_of[pre_node]:
            if pre_bit >> cur_node & 1 == 0:
                # cur_nodeは未訪問
                cur_bit = pre_bit ^ (1 << cur_node)
                ret = min(dfs(cur_bit, cur_node, DP) + d, ret)
        DP[pre_bit][pre_node] = ret
        return ret

    ans = dfs(0, 0, DP)
    if ans == INF:
        print(-1)
    else:
        print(ans)


main()
