import heapq as hp
# ダイクストラ
# 1->kの最短距離と、n->kの最短距離の和となる


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, c))
        nei_of[b].append((a, c))

    # ダイクストラ二回
    def dijkstra(st_node, D):
        que = []
        # st_node = (0, 0)
        hp.heappush(que, st_node)
        while que:
            pre_dist, pre_node = hp.heappop(que)
            if pre_dist > D[pre_node]:
                continue
            for cur_node, cur_dist in nei_of[pre_node]:
                d = pre_dist + cur_dist
                if D[cur_node] > d:
                    D[cur_node] = d
                    hp.heappush(que, (d, cur_node))

    st_node = (0, 0)
    D = [float('inf')] * node_end
    D[0] = 0
    dijkstra(st_node, D)

    st_node = (0, node_end - 1)
    D2 = [float('inf')] * node_end
    D2[node_end-1] = 0
    dijkstra(st_node, D2)

    for k in range(node_end):
        print(D[k]+D2[k])


main()
