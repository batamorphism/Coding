from collections import deque
# 距離が偶数か奇数か
# dist[fr][to] = dist[head][to] + dist[head][fr] - dist[head][lca]*2
# したがって、mod2上では
# dist[fr][to] = dist[head][to] + dist[head][fr]
# よって、head_nodeからの距離の和が偶数ならばTown, 奇数ならばRoad
def main():
    INF = float('inf')
    n, q = map(int, input().split())
    nei_of = [[] for _ in range(n)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)

    # calc_dist
    # BFS
    dist = [INF]*n
    que = deque()
    head_node = 0
    que.append(head_node)
    dist[head_node] = 0

    while que:
        pre = que.popleft()
        d = dist[pre]
        d += 1
        for cur in nei_of[pre]:
            if dist[cur] <= d:
                continue
            dist[cur] = d
            que.append(cur)

    ans_list = []
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        dist_sum = dist[c] + dist[d]
        if dist_sum % 2 == 0:
            ans = 'Town'
        else:
            ans = 'Road'
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
