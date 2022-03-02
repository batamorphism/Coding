from collections import deque


# ハミルトン経路
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)

    k = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))

    # c_i -> c_j の距離をdist_c[i][j] に格納
    INF = float('inf')
    dist_c = [[INF] * k for _ in range(k)]

    for i, c_i in enumerate(C):
        que = deque([c_i])
        dist = [INF] * node_end
        dist[c_i] = 0
        while que:
            pre = que.popleft()
            cur_d = dist[pre]+1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        for j, c_j in enumerate(C):
            dist_c[i][j] = dist[c_j]

    ALL = 1 << k
    # DP[S][node] Sを探索済みで、現在nodeにいるときの、既に使った石の数の最小値
    DP = [[INF]*k for _ in range(ALL)]
    # 配るDP
    for cur_S in range(ALL):
        for cur_node in range(k):
            DP[1 << cur_node][cur_node] = 1
            if cur_S >> cur_node & 1 == 0:
                continue
            for nex_node in range(k):
                nex_S = cur_S | 1 << nex_node
                cost = dist_c[cur_node][nex_node]
                DP[nex_S][nex_node] = min(DP[nex_S][nex_node], DP[cur_S][cur_node] + cost)

    ans = min(DP[ALL-1])
    if ans == INF:
        ans = -1
    print(ans)


main()
