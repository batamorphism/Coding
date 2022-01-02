from itertools import product
INF = float('inf')


# ワーシャルフロイド
def main():
    node_end, edge_end = map(int, input().split())
    adj = [[INF]*node_end for _ in range(node_end)]

    for _ in range(edge_end):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        adj[a][b] = c

    for node in range(node_end):
        adj[node][node] = 0

    dist = adj
    ans = 0
    iter = product(range(node_end), repeat=3)
    for k, fr, to in iter:
        d1 = dist[fr][to]
        d3 = dist[fr][k] + dist[k][to]
        d = min(d1, d3)
        dist[fr][to] = d
        if d != INF and d != 0:
            ans += d

    print(ans)


main()
