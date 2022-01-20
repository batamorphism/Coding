import imp
from itertools import product


# 2点間最小距離
# 1->fr
# 1->to
# fr -> to (ただし途中で1は経由しない)
def main():
    INF = float('inf')
    node_end, edge_end = map(int, input().split())

    adj = [[INF]*node_end for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to, di = map(int, input().split())
        fr -= 1
        to -= 1
        adj[fr][to] = di
        adj[to][fr] = di

    dist = [[INF]*node_end for _ in range(node_end)]
    for fr, to in product(range(1, node_end), repeat=2):
        # 0を経由する場合は無視する
        dist[fr][to] = adj[fr][to]
        dist[to][fr] = adj[fr][to]

    # ワーシャルフロイド
    for k, fr, to in product(range(node_end), repeat=3):
        dist[fr][to] = min(dist[fr][to], dist[fr][k] + dist[k][to])

    ans = INF
    for fr, to in product(range(1, node_end), repeat=2):
        if fr == to:
            continue
        d1 = adj[0][fr]
        d2 = dist[fr][to]
        d3 = adj[to][0]
        if d1+d2+d3 == 10:
            print(fr, to)
        ans = min(ans, d1+d2+d3)

    if ans == INF:
        ans = -1
    print(ans)


main()
