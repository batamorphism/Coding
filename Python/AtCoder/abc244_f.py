from collections import deque
import heapq


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # bitDP
    # 配るDP
    ALL = 1 << node_end
    INF = float('inf')
    dist = [INF]*ALL  # 現在使った頂点
    dist[0] = 0
    DP = [INF]*ALL  # 答え
    DP[0] = 0

    que = []
    # (距離, 現在使った頂点, 頂点の偶奇)
    for node in range(node_end):
        DP[1 << node] = 1
        dist[1 << node] = 1
        heapq.heappush(que, (1, 1 << node, 1 << node))

    while que:
        pre_d, pre_use_S, pre_S = heapq.heappop(que)
        if dist[pre_use_S] < pre_d and DP[pre_S] < pre_d:
            continue
        for node in range(node_end):
            if (1 << node) & pre_use_S == 0:
                continue
            for cur_node in nei_of[node]:
                cur_use_S = pre_use_S | (1 << cur_node)
                cur_S = pre_S ^ (1 << cur_node)
                if DP[cur_S] <= pre_d + 1 and dist[cur_use_S] <= pre_d + 1:
                    continue
                dist[cur_use_S] = min(pre_d + 1, dist[cur_use_S])
                DP[cur_S] = min(DP[cur_S], pre_d + 1)
                heapq.heappush(que, (pre_d+1, cur_use_S, cur_S))

    ans = 0
    for S in range(ALL):
        ans += DP[S]

    print(ans)


main()
