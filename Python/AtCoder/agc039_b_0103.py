# V_i の集合は、あるrootからの距離がiとなるnodeからなる?
# 集合の個数は最大化させるため、V_i = root空の距離がi としてよい
# ただし、2部グラフでないときは、rootからの距離の偶奇が同じもの同士でのedgeが存在してしまう
# 明らかに、これは距離が同じ場合しかありえないので、題意に反する
# 2部グラフの時は、rootからの距離のが同じもの同士でのedgeが存在しない。したがって題意を満たす
from collections import deque
from itertools import product
INF = float('inf')


def main():
    node_end = int(input())
    adj = [list(map(int, input())) for _ in range(node_end)]

    if not is_bipartite(adj, node_end):
        print(-1)
        return

    dist = [[INF]*node_end for _ in range(node_end)]
    for r, c in product(range(node_end), repeat=2):
        if adj[r][c]:
            dist[r][c] = 1
        if r == c:
            dist[r][c] = 0

    # ワーシャルフロイド
    for k, fr, to in product(range(node_end), repeat=3):
        d1 = dist[fr][to]
        d2 = dist[fr][k] + dist[k][to]
        dist[fr][to] = min(d1, d2)

    # 直径
    diameter = -INF
    for fr, to in product(range(node_end), repeat=2):
        if dist[fr][to] > diameter:
            diameter = dist[fr][to]

    print(diameter+1)


def is_bipartite(adj, node_end):
    color_of = [-1] * node_end
    root = 0
    color_of[root] = 0
    que = deque()
    que.append(root)
    while que:
        pre = que.popleft()
        pre_color = color_of[pre]
        cur_color = 1 ^ pre_color
        for cur, is_edge in enumerate(adj[pre]):
            if not is_edge:
                continue
            if color_of[cur] == -1:
                color_of[cur] = cur_color
                que.append(cur)
            else:
                if color_of[cur] != cur_color:
                    return False
    return True


main()
