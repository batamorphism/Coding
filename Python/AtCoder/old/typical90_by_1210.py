import networkx as nx
from collections import defaultdict


def main():
    n, t = map(int, input().split())
    dxy_list = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    A = []
    B = []

    for _ in range(n):
        ax, ay = map(int, input().split())
        A.append((ax, ay))
    for _ in range(n):
        bx, by = map(int, input().split())
        B.append((bx, by))

    # t秒前にbがいた位置の候補
    # [(x, y)] = Bのindのset
    bxy_before = defaultdict(set)
    for i, bxy in enumerate(B):
        x, y = bxy
        for dxy in dxy_list:
            dx, dy = dxy
            pre_x, pre_y = x - dx*t, y - dy*t
            bxy_before[(pre_x, pre_y)].add(i)

    G = nx.Graph()
    # AとBとの考えうる組み合わせをedgeにする
    # nodeは、(i, 0or1)の形にしてみる
    for a_or_b in range(2):
        for i in range(n):
            G.add_node((i, a_or_b), bipartite=a_or_b)

    for ai, axy in enumerate(A):
        x, y = axy
        for bi in bxy_before[axy]:
            G.add_edge((ai, 0), (bi, 1))

    # matched_B_of[ai] = aiとマッチしたbi
    matched_B_of = [-1]*n
    for comp in nx.connected_components(G):
        # 各連結成分ごとに、最大マッチングを求める
        # S = G.subgraph(comp).copy()
        Sd = nx.bipartite.maximum_matching(G.subgraph(comp))
        for key, item in Sd.items():
            i_0, a_or_b_0 = key
            i_1, a_or_b_1 = item
            if a_or_b_0 == 0:
                # 0がa
                matched_B_of[i_0] = i_1
            else:
                matched_B_of[i_1] = i_0

    if min(matched_B_of) == -1:
        print('No')
        return
    else:
        print('Yes')

    def calc_ori(axy, bxy):
        ax, ay = axy
        bx, by = bxy
        for ori in range(8):
            dx, dy = dxy_list[ori]
            if ax + dx*t == bx and ay + dy*t == by:
                return ori+1

    for i_a, axy in enumerate(A):
        i_b = matched_B_of[i_a]
        bxy = B[i_b]
        print(calc_ori(axy, bxy))


main()
