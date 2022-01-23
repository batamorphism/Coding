from collections import deque
from itertools import product


# 二部グラフでないなら-1
# 直径を求める
def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for fr in range(n):
        adj = list(map(int, input()))
        for to, is_connect in enumerate(adj):
            if is_connect:
                nei_of[fr].append(to)

    if not bipartite(n, nei_of):
        print(-1)
        return

    # 直径を求める
    # 木じゃないので、Warshall-Floydを使う
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]
    for fr in range(n):
        dist[fr][fr] = 0
        for to in nei_of[fr]:
            dist[fr][to] = 1

    for k, fr, to in product(range(n), repeat=3):
        dist[fr][to] = min(dist[fr][to], dist[fr][k] + dist[k][to])

    ans = -1
    for fr, to in product(range(n), repeat=2):
        ans = max(ans, dist[fr][to])

    print(ans+1)


def bipartite(n, nei_of):
    color = [-1] * n
    color[0] = 0
    que = deque()
    que.append(0)
    while que:
        pre = que.popleft()
        pre_c = color[pre]
        cur_c = 1 - pre_c
        for cur in nei_of[pre]:
            if color[cur] == -1:
                color[cur] = cur_c
                que.append(cur)
            else:
                if color[cur] != cur_c:
                    return False
    return True


main()
