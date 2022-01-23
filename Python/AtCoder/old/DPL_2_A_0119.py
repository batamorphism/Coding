# 配るDP
# S:既に通った頂点、a:まだ通ってない頂点、i:今いる頂点
# DP[S][i] 既にSを通っており、現在iにいる状態における、今までの経路の最短値
# DP[null][0] = 0
# DP[ALL][0] = 答え
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to, di = map(int, input().split())
        nei_of[fr].append((to, di))

    INF = float('inf')
    ALL = 1 << node_end
    DP = [[INF] * node_end for _ in range(ALL)]
    DP[0][0] = 0

    for cur_S in range(ALL):
        for i in range(node_end):
            for a, di in nei_of[i]:
                # a not in Sの場合のみ処理
                if (cur_S >> a) & 1:
                    continue
                nex_S = cur_S | (1 << a)
                DP[nex_S][a] = min(DP[nex_S][a], DP[cur_S][i] + di)

    ans = DP[ALL-1][0]
    if ans == INF:
        ans = -1
    print(ans)


main()
