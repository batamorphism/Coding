# ダイクストラ
import heapq as hp
INF = float('inf')


def main():
    node_end, k = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]

    ans_list = []
    for _ in range(k):
        ip = list(map(int, input().split()))
        if ip[0] == 0:
            # 注文票
            fr = ip[1]-1
            to = ip[2]-1
            ans = dijkstra(nei_of, fr, to)
            ans_list.append(ans)
        else:
            # 開通
            fr = ip[1]-1
            to = ip[2]-1
            co = ip[3]
            nei_of[fr].append((to, co))
            nei_of[to].append((fr, co))
    print(*ans_list, sep='\n')


def dijkstra(nei_of, fr, to):
    node_end = len(nei_of)
    dist = [INF] * node_end

    que = [(0, fr)]
    dist[fr] = 0
    while que:
        pre_d, pre_node = hp.heappop(que)
        if dist[pre_node] < pre_d:
            continue
        for cur, cost in nei_of[pre_node]:
            d = pre_d + cost
            if dist[cur] <= d:
                continue
            dist[cur] = d
            hp.heappush(que, (d, cur))

    ret = dist[to]
    if ret == INF:
        ret = -1
    return ret


main()
