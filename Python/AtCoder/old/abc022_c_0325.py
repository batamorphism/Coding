# 1を通らないで、全点間距離を求める
def main():
    node_end, edge_end = map(int, input().split())
    INF = float('inf')
    nei_of = [[] for _ in range(node_end)]
    adj = [[INF]*node_end for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append((to, cost))
        nei_of[to].append((fr, cost))
        adj[fr][to] = cost
        adj[to][fr] = cost

    dist = [[INF]*node_end for _ in range(node_end)]
    for fr in range(node_end):
        for to in range(node_end):
            if fr != 0 and to != 0:
                dist[fr][to] = adj[fr][to]

    # ワーシャルフロイド法
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                dist[fr][to] = min(dist[fr][to], dist[fr][k] + dist[k][to])

    ans = INF
    for fr, cost_fr in nei_of[0]:
        for to, cost_to in nei_of[0]:
            if fr == to:
                continue
            # fr->toとなる、0を通らない経路の距離
            cost_mid = dist[fr][to]
            cost_total = cost_fr + cost_to + cost_mid
            ans = min(ans, cost_total)

    if ans == INF:
        ans = -1
    print(ans)


main()
