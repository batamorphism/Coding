def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        fr, to, di = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append((to, di))
        nei_of[to].append((fr, di))

    INF = float('inf')
    # Dist_2p[fr][to] = frからtoへの距離、他の頂点は通らない
    # Dist[fr][to] = frからtoへの最短距離、ただし0は通らない
    Dist_2p = [[INF]*node_end for _ in range(node_end)]
    Dist = [[INF]*node_end for _ in range(node_end)]

    for fr in range(node_end):
        for to, di in nei_of[fr]:
            Dist_2p[fr][to] = di

    # ワーシャルフロイド
    # node1を通らない前提で、frからtoへの最短距離を求める
    for k in range(1, node_end):
        for fr in range(1, node_end):
            for to in range(1, node_end):
                d1 = Dist[fr][to]
                d2 = Dist[fr][k] + Dist[k][to]
                d3 = Dist_2p[fr][to]
                Dist[fr][to] = min(d1, d2, d3)

    ans = INF
    for first in range(node_end):
        for last in range(node_end):
            if first == last:
                continue
            pre_ans = Dist_2p[0][first] + Dist[first][last] + Dist_2p[last][0]
            ans = min(ans, pre_ans)

    if ans == INF:
        ans = -1

    print(ans)


main()
