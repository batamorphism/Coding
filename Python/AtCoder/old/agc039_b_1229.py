# 2部グラフでないならば不可能
# 最も端の頂点sと、sからの距離d_iを考えると
# 距離d_iのものを集合V_(d_i)に入れれば、条件を満たす
from collections import deque


def main():
    node_end = int(input())
    INF = float('inf')
    adj_mat = [list(map(int, input())) for _ in range(node_end)]
    # 隣接行列から、距離の行列に変換
    for r in range(node_end):
        for c in range(node_end):
            if adj_mat[r][c] == 0:
                adj_mat[r][c] = INF
            if r == c:
                adj_mat[r][c] = 0

    nei_of = [[] for _ in range(node_end)]
    for fr, to_list in enumerate(adj_mat):
        for to, val in enumerate(to_list):
            if val != 1:
                continue
            nei_of[fr].append(to)

    # 2部グラフか判定
    color = [-1] * node_end
    st_node = 0
    color[st_node] = 0
    que = deque()
    que.append(st_node)
    while que:
        pre = que.pop()
        pre_col = color[pre]
        cur_col = pre_col ^ 1
        for cur in nei_of[pre]:
            if color[cur] == -1:
                color[cur] = cur_col
                que.append(cur)
            else:
                # 彩色が矛盾しないか判定
                if color[cur] != cur_col:
                    print('-1')
                    return

    # 2点間距離を求める
    dist = [[INF]*node_end for _ in range(node_end)]
    for k in range(node_end):
        for fr in range(node_end):
            for to in range(node_end):
                d1 = dist[fr][to]
                d2 = adj_mat[fr][to]
                d3 = dist[fr][k] + dist[k][to]
                dist[fr][to] = min(d1, d2, d3)

    dia = 0  # 直径
    for fr in range(node_end):
        for to in range(node_end):
            d = dist[fr][to]
            if d > dia:
                dia = d

    print(dia+1)


main()
