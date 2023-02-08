# ワーシャルフロイド法
def main():
    node_end, edge_end = map(int, input().split())
    INF = float('inf')
    adj = [[INF]*node_end for _ in range(node_end)]
    for node in range(node_end):
        adj[node][node] = 0

    for _ in range(edge_end):
        fr, to, co = map(int, input().split())
        fr -= 1
        to -= 1
        adj[fr][to] = co

    ans = 0
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                adj[fr][to] = min(adj[fr][to], adj[fr][k] + adj[k][to])
                cur_ans = adj[fr][to]
                if cur_ans == INF:
                    continue
                if fr == to:
                    continue
                ans += cur_ans

    print(ans)


main()
