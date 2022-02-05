from collections import deque


# 直径はdfs2回
def main():
    n = int(input())
    nbh_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nbh_of[a].append(b)
        nbh_of[b].append(a)

    INF = float('inf')
    head_node = 0
    for _ in range(2):
        dist = [INF]*n
        que = deque()
        que.append(head_node)
        dist[head_node] = 0
        while que:
            pre = que.popleft()
            for cur in nbh_of[pre]:
                if dist[cur] == INF:
                    dist[cur] = dist[pre] + 1
                    que.append(cur)
        far_node = -1
        max_dist = max(dist)
        for node, d in enumerate(dist):
            if d == max_dist:
                far_node = node
                break
        head_node = far_node

    ans = dist[head_node] + 1
    print(ans)


main()
