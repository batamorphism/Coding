from collections import deque


def main():
    node_end = int(input())
    grid = [list(map(int, input())) for _ in range(node_end)]

    INF = float('inf')
    # 2部グラフであることが、作るための必要十分条件
    nei_of = [[] for _ in range(node_end)]
    for fr in range(node_end):
        for to in range(node_end):
            if grid[fr][to]:
                nei_of[fr].append(to)
    # 与えられるグラフは連結である
    que = deque([0])
    col = [-1] * node_end
    col[0] = 0
    is_bipartite = True
    # DFS
    while que:
        pre = que.pop()
        pre_col = col[pre]
        cur_col = 1 ^ pre_col
        for cur in nei_of[pre]:
            if col[cur] != -1:
                if col[cur] != cur_col:
                    is_bipartite = False
                    break
                continue
            col[cur] = cur_col
            que.append(cur)
    if not is_bipartite:
        print(-1)
        return

    # 全点間距離の最大値+1が答え
    dist = [[INF]*node_end for _ in range(node_end)]
    for fr in range(node_end):
        dist[fr][fr] = 0
        for to in range(node_end):
            if grid[fr][to]:
                dist[fr][to] = 1

    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                d1 = dist[fr][to]
                d2 = dist[fr][k] + dist[k][to]
                dist[fr][to] = min(d1, d2)

    max_dist = -INF
    for fr in range(node_end):
        for to in range(node_end):
            max_dist = max(max_dist, dist[fr][to])

    ans = max_dist+1
    print(ans)


main()
