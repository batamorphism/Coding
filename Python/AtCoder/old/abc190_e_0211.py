# ハミルトン経路問題
from collections import deque
from collections import defaultdict


def calc_dist_2p(node_end, edge_list, C):
    nei_of = [[] for _ in range(node_end)]
    for fr, to in edge_list:
        nei_of[fr].append(to)
        nei_of[to].append(fr)
    INF = float('inf')
    dist_2p = [[INF]*len(C) for _ in range(len(C))]
    for i, fr in enumerate(C):
        dist = [INF]*node_end
        dist[fr] = 0
        que = deque([fr])
        while que:
            pre = que.popleft()
            cur_d = dist[pre] + 1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        for j, to in enumerate(C):
            dist_2p[i][j] = dist[to]
    return dist_2p


def main():
    node_end, edge_end = map(int, input().split())
    edge_list = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(edge_end)]

    k = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))
    dist_2p = calc_dist_2p(node_end, edge_list, C)

    INF = float('inf')
    nei_of = [[] for _ in range(k)]

    for i, fr in enumerate(C):
        for j, to in enumerate(C):
            if dist_2p[i][j] != INF:
                d = dist_2p[i][j]
                nei_of[i].append((j, d))

    # 全点を通る、最短回路を求める
    ALL = 1 << k
    dist = [[INF]*k for _ in range(ALL)]

    for cur_S in range(ALL):
        for cur_node in range(k):
            dist[1 << cur_node][cur_node] = 0
            if cur_S >> cur_node & 1 == 0:
                continue
            for nex_node, nex_cost in nei_of[cur_node]:
                nex_S = cur_S | 1 << nex_node
                nex_dist = dist[cur_S][cur_node] + nex_cost
                dist[nex_S][nex_node] = min(dist[nex_S][nex_node], nex_dist)

    ans = min(dist[ALL-1]) + 1
    if ans == INF:
        ans = -1
    print(ans)


main()
