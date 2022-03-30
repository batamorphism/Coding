from collections import deque

# ハミルトン経路
def main():
    n, m = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    INF = float('inf')

    for _ in range(m):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    k = int(input())
    c_dist = [[INF]*k for _ in range(k)]
    C = list(map(lambda x: int(x)-1, input().split()))

    # 各Cの間の最短距離を求める
    for i, c_i in enumerate(C):
        dist = [INF]*n
        dist[c_i] = 0
        que = deque([c_i])
        while que:
            pre = que.popleft()
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        for j, c_j in enumerate(C):
            c_dist[i][j] = dist[c_j]

    # c_distを使って、最短回路を求める
    # 配るDP
    # DP[bit][node] bitを探索済みで、現在nodeにいる状態での最小コスト
    ALL = 1 << k
    DP = [[INF]*k for _ in range(ALL)]
    for pre_S in range(ALL):
        for pre_node in range(k):
            if pre_S == 0:
                DP[pre_S][pre_node] = 1
            for cur_node in range(k):
                cur_S = pre_S | (1 << cur_node)
                DP[cur_S][cur_node] = min(DP[cur_S][cur_node], DP[pre_S][pre_node] + c_dist[pre_node][cur_node])
    ans = min(DP[ALL-1])
    if ans == INF:
        ans = -1
    print(ans)


main()
