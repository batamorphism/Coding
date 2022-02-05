from collections import deque
from collections import defaultdict

# ハミルトン経路問題
def main():
    node_end, edge_end = map(int, input().split())
    nhd_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nhd_of[fr].append(to)
        nhd_of[to].append(fr)
    k = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))

    INF = float('inf')
    dist_c_of = defaultdict(lambda: INF)

    # 各c_i, c_jの距離を求める
    for c_fr in C:
        dist = [INF]*node_end
        dist[c_fr] = 0
        que = deque([c_fr])
        while que:
            pre = que.popleft()
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur in nhd_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)

        for c_to in C:
            d = dist[c_to]
            dist_c_of[(c_fr, c_to)] = min(dist_c_of[(c_fr, c_to)], d)
            dist_c_of[(c_to, c_fr)] = min(dist_c_of[(c_to, c_fr)], d)

    # Cだけに座圧した新しいグラフをつくる
    node_end = k
    dist = [[INF]*node_end for _ in range(node_end)]
    for i, c_i in enumerate(C):
        for j, c_j in enumerate(C):
            dist[i][j] = dist_c_of[(c_i, c_j)]

    ALL = 1 << node_end
    DP = [[INF] * node_end for _ in range(ALL)]
    for begin_node in range(node_end):
        DP[1 << begin_node][begin_node] = 0
    for cur_S in range(ALL):
        for cur_node in range(node_end):
            if cur_S >> cur_node & 1 == 0:
                continue
            for nex_node in range(node_end):
                nex_S = cur_S | (1 << nex_node)
                DP[nex_S][nex_node] = min(DP[nex_S][nex_node], DP[cur_S][cur_node] + dist[cur_node][nex_node])

    ans = min(DP[ALL-1]) + 1
    if ans == INF:
        ans = -1
    print(ans)


main()
