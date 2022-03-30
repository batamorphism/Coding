import copy


# 全点間距離が変わらないように辺を削除する
# 迂回路がある場合は削除可能
def main():
    node_end, edge_end = map(int, input().split())
    INF = float('inf')
    adj = [[INF]*node_end for _ in range(node_end)]
    edge_list = []
    for _ in range(edge_end):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        adj[fr][to] = cost
        adj[to][fr] = cost
        edge_list.append((fr, to, cost))

    for node in range(node_end):
        adj[node][node] = 0
    dist = copy.deepcopy(adj)

    # 全点間距離を計算する
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                dist[fr][to] = min(dist[fr][to], dist[fr][k]+dist[k][to])

    delete_edge_cnt = 0
    for fr, to, cost in edge_list:
        # 他に最短距離があるときは削除可能
        if cost > dist[fr][to]:
            delete_edge_cnt += 1
            continue
        # cost == distの場合、同じ距離の迂回路があれば削除可能
        another_cost = INF
        for k in range(node_end):
            if k != fr and k != to:
                another_cost = min(another_cost, dist[fr][k]+dist[k][to])
        if cost == another_cost:
            delete_edge_cnt += 1
    print(delete_edge_cnt)


main()
