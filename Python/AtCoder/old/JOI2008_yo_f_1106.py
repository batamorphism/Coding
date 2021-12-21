import heapq as hq
INF = 10**12


def main():
    node_end, k = map(int, input().split())
    # (node, cost)
    nei_of = [[] for _ in range(node_end)]
    ans = []
    for _ in range(k):
        ip = list(map(int, input().split()))
        if ip[0] == 0:
            # 移動開始
            # ダイクストラ
            fr, to = ip[1], ip[2]
            fr -= 1
            to -= 1
            cost = dijkstra(fr, to, node_end, nei_of)
            ans.append(cost)
        else:
            # edge追加
            fr, to, cost = ip[1], ip[2], ip[3]
            fr -= 1
            to -= 1
            nei_of[fr].append((to, cost))
            nei_of[to].append((fr, cost))

    for a in ans:
        print(a)


def dijkstra(fr, to, node_end, nei_of):
    dist = [INF] * node_end
    dist[fr] = 0
    que = [(0, fr)]
    while que:
        pre = hq.heappop(que)
        pre_dist, pre_node = pre
        d = dist[pre_node]
        if pre_dist > d:
            continue
        if pre_node == to:
            return d
        for cur in nei_of[pre_node]:
            cur_node, cur_dist = cur
            if dist[cur_node] > d + cur_dist:
                dist[cur_node] = d + cur_dist
                hq.heappush(que, (d + cur_dist, cur_node))
    return -1


main()
