import Python.AtCoder.pypyjit as pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
pypyjit.set_param('disable_unrolling=-1')
# bit-DP
def main():
    # input
    n, k = map(int, input().split())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    INF = 2*10**18+1
    max_dist = 0
    # dist_2p[p1][p2] = p1,p2の2点間の距離
    dist_2p = [[0]*n for _ in range(n)]
    for p1_i, p1 in enumerate(points):
        for p2_i, p2 in enumerate(points):
            x1, y1 = p1
            x2, y2 = p2
            dist_2p[p1_i][p2_i] = (x2-x1)**2+(y2-y1)**2
            max_dist = max(dist_2p[p1_i][p2_i], max_dist)

    MAX = 1 << n  # MAX<=32,768
    # dist[bit] = 各グループbitの距離の最大値
    dist = [INF]*(MAX)
    for bit in range(MAX):
        p_list = []
        for point in range(n):
            if bit >> point & 1:
                p_list.append(point)
        if len(p_list) <= 1:
            dist[bit] = 0
            continue
        d = 0
        for p1 in p_list:
            for p2 in p_list:
                if p2 > p1:
                    break
                d = max(d, dist_2p[p1][p2])
        dist[bit] = d

    # bit-DP
    # DP[bit][grp] = 現在、bitの点をgrp個に分割して選んでいる状態での、各グループ内の距離の最大値の最小値
    # 答えはbit[MAX][k]になる
    DP = [[INF]*(k+1) for _ in range(MAX)]
    DP[0][0] = 0
    for bit in range(1, MAX):
        p_cnt = 0
        for i in range(n):
            if (bit >> i & 1):
                p_cnt += 1
        for grp in range(1, min(k, p_cnt)+1):
            sub_bit = bit  # bitの部分集合
            com_bit = 0    # bit-sub_bit
            while sub_bit:
                sub_bit = (sub_bit-1) & bit
                com_bit = bit ^ sub_bit
                DP[bit][grp] = min(max(DP[sub_bit][grp-1], dist[com_bit]), DP[bit][grp])

    print(DP[-1][-1])


main()
