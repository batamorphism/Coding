# node c_0, ..., c_k-1 を含む最小の部分グラフを求める
# 各c_i, c_jの距離を求め・・・
# 最短ハミルトン路問題
# DP[S][node] := Sの各頂点を含み、nodeで終わるパスの長さの最小値
# 答えは、min(DP[C][i])+1
from collections import deque


def main():
    # get_input
    node_end, edge_end = map(int, input().split())
    nbh_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nbh_of[fr].append(to)
        nbh_of[to].append(fr)
    c_end = int(input())
    C = list(map(lambda x: int(x)-1, input().split()))

    # setup_variables
    INF = 10**7
    ALL = 1 << c_end
    DP = [[INF]*c_end for _ in range(ALL)]
    for node in range(c_end):
        DP[1 << node][node] = 0
    # Cに含まれる2点間の距離
    dist_C_of = [[INF]*c_end for _ in range(c_end)]

    # calc_dist_C_of
    for st_i, st in enumerate(C):
        dist = [INF]*node_end
        dist[st] = 0
        que = deque([st])
        while que:
            pre = que.popleft()
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur in nbh_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
        for en_i, en in enumerate(C):
            dist_C_of[st_i][en_i] = dist[en]
            dist_C_of[en_i][st_i] = dist[en]

    # calc_DP
    for cur_S in range(ALL):
        for cur_node in range(c_end):
            if cur_S >> cur_node & 1 == 0:
                continue
            for nex_node in range(c_end):
                nex_S = cur_S | (1 << nex_node)
                cost = dist_C_of[cur_node][nex_node]
                DP[nex_S][nex_node] = min(DP[nex_S][nex_node], DP[cur_S][cur_node] + cost)

    ans = min(DP[ALL-1]) + 1
    if ans >= INF//2:
        ans = -1
    print(ans)


main()
