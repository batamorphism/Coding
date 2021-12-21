from collections import deque


# 完全グラフはハブに
def main():
    INF = float('inf')

    node_end, m = map(int, input().split())
    n = node_end
    nei_of = [[] for _ in range(node_end)]
    for _ in range(m):
        k = int(input())
        R = list(map(int, input().split()))
        R = [r-1 for r in R]
        hub = node_end
        nei_of.append([])
        node_end += 1
        for node in R:
            nei_of[hub].append(node)
            nei_of[node].append(hub)

    # dfs
    que = deque()
    dist = [INF]*node_end
    que.append(0)
    dist[0] = 0
    while que:
        pre = que.popleft()
        pre_d = dist[pre]
        d = pre_d + 1
        for cur in nei_of[pre]:
            if dist[cur] > d:
                dist[cur] = d
                que.append(cur)

    for node in range(n):
        ans = dist[node]
        if ans == INF:
            ans = -1
        else:
            ans //= 2
        print(ans)


main()
