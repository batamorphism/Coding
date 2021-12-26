# 0 -> fr
# to -> 0の距離(fr != to)と
# fr -> toの距離の合計が最小となるもの
# ワーシャルフロイド
def main():
    node_end, edge_end = map(int, input().split())
    INF = float('inf')
    adj_matrix = [[INF]*node_end for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        adj_matrix[fr][to] = cost
        adj_matrix[to][fr] = cost

    dist = [[INF]*node_end for _ in range(node_end)]
    for k in range(1, node_end):
        for fr in range(1, node_end):
            for to in range(1, node_end):
                dist[fr][to] = min(dist[fr][to], dist[fr][k] + dist[k][to], adj_matrix[fr][to])

    ans = INF
    for fr in range(1, node_end):
        for to in range(1, node_end):
            if fr == to:
                continue
            cost_fr = adj_matrix[0][fr]
            cost_to = adj_matrix[to][0]
            cost_fr_to = dist[fr][to]
            cost = cost_fr + cost_to + cost_fr_to
            ans = min(ans, cost)

    if ans == INF:
        ans = -1
    print(ans)


main()
