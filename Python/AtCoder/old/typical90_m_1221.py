# n <= 10**5
# ダイクストラ
# 1 -> kの最短経路と、k -> nの最短経路の和が答え
# 1 -> kの最短経路と、 n-> kの最短経路をあらかじめ求めておけばよい
import heapq as hp


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    INF = float('inf')

    for _ in range(edge_end):
        fr, to, cost = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append((cost, to))
        nei_of[to].append((cost, fr))

    dist0 = [INF]*node_end
    dist1 = [INF]*node_end
    dijkstra(nei_of, 0, dist0)
    dijkstra(nei_of, node_end-1, dist1)

    for k in range(node_end):
        ans = dist0[k] + dist1[k]
        print(ans)


def dijkstra(nei_of, start, dist):
    dist[start] = 0
    que = []
    hp.heappush(que, (0, start))
    while que:
        pre_cost, pre_node = hp.heappop(que)
        if pre_cost > dist[pre_node]:
            continue
        for cost, cur_node in nei_of[pre_node]:
            cur_cost = pre_cost + cost
            if cur_cost >= dist[cur_node]:
                continue
            dist[cur_node] = cur_cost
            hp.heappush(que, (cur_cost, cur_node))


main()
