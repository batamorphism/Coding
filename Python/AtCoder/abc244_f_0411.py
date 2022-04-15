from collections import deque


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        nei_of[to].append(fr)

    # dist[S][node]
    S_end = 1 << node_end
    INF = float('inf')
    dist = [[INF]*node_end for _ in range(S_end)]

    # BFS
    # que[0] = (S, node)
    que = deque()
    for node in range(node_end):
        S = 1 << node
        que.append((S, node))
        dist[S][node] = 1

    while que:
        pre_S, pre_node = que.popleft()
        pre_d = dist[pre_S][pre_node]
        cur_d = pre_d + 1
        for cur_node in nei_of[pre_node]:
            cur_S = pre_S ^ (1 << cur_node)
            if dist[cur_S][cur_node] <= cur_d:
                continue
            dist[cur_S][cur_node] = cur_d
            que.append((cur_S, cur_node))

    dist[0][0] = 0
    ans = 0
    for S in range(S_end):
        ans += min(dist[S])
    print(ans)


main()
