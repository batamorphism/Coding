from collections import deque


# ハミルトン経路問題
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        nei_of[b].append(a)
    k = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))
    INF = float('inf')

    dist_c = [[INF]*k for _ in range(k)]

    # 各c_iからc_jへの最短距離を求める
    for fr, c_fr in enumerate(C):
        dist = [INF]*node_end
        dist[c_fr] = 0
        que = deque([c_fr])
        while que:
            pre = que.popleft()
            cur_d = dist[pre] + 1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        for to, c_to in enumerate(C):
            dist_c[fr][to] = dist[c_to]

    ans = hamilton(k, dist_c)
    ans += 1
    if ans == INF:
        ans = -1
    print(ans)


def hamilton(node_end, dist):
    ALL = 1 << node_end
    INF = float('inf')
    # DP[S][node]
    DP = [[INF]*node_end for _ in range(ALL)]
    for cur_node in range(node_end):
        DP[1 << cur_node][cur_node] = 0
    for cur_S in range(ALL):
        for cur_node in range(node_end):
            if cur_S >> cur_node & 1 == 0:
                continue
            for nex_node in range(node_end):
                cost = dist[cur_node][nex_node]
                nex_S = cur_S | (1 << nex_node)
                DP[nex_S][nex_node] = min(DP[nex_S][nex_node], DP[cur_S][cur_node] + cost)

    ans = INF
    for cur_node in range(node_end):
        ans = min(ans, DP[ALL-1][cur_node])
    return ans


main()
