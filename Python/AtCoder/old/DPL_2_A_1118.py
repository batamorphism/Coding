INF = 10**9


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        s, t, d = map(int, input().split())
        nei_of[s].append((t, d))

    ALL = 1 << node_end
    D = [[-1]*node_end for _ in range(ALL)]

    def dfs(bit, node):
        # 現在bitを探索済み
        # nodeにいる状態
        # ここから、残りを探索して0に戻るのにかかるコスト
        if D[bit][node] != -1:
            return D[bit][node]
        if bit == ALL-1 and node == 0:
            return 0
        ret = INF
        for nex in nei_of[node]:
            nex_node, nex_d = nex
            # 既にbitを探索済みであれば飛ばす
            if (bit >> nex_node) & 1:
                continue
            # nex_nodeに行った場合のコストを計算
            nex_bit = bit | (1 << nex_node)
            cost = dfs(nex_bit, nex_node) + nex_d
            ret = min(ret, cost)
        D[bit][node] = ret
        return ret

    ans = dfs(0, 0)
    if ans == INF:
        ans = -1
    print(ans)
    # print(D)


main()
