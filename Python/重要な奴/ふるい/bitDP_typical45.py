def main():
    n, k = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(n)]

    # dist[p1][p2] = p1とp2の距離
    dist = [[0]*n for _ in range(n)]
    for p1 in range(n):
        for p2 in range(n):
            dist[p1][p2] = (XY[p1][0]-XY[p2][0])**2 + (XY[p1][1]-XY[p2][1])**2

    INF = 2*10**18+1  # ギリギリの数にしないとTLEする
    ALL = 1 << n

    # calc dist_bit
    # dist_bit[選んだ点]の2点間距離の最大値
    dist_bit = [INF]*ALL
    for bit in range(ALL):
        p_list = []
        for i in range(n):
            if (bit >> i & 1):
                p_list.append(i)
        d = 0
        for p1 in p_list:
            for p2 in p_list:
                if p2 > p1:
                    break
                d = max(dist[p1][p2], d)
        dist_bit[bit] = d

    # calc bitDP
    # DP[既に選んだ点][現在のグループ]のスコアの最小値 = 部分点に対し、max(DP[sub_bit][group-1], dist[bit^sub_bit])
    DP = [[INF]*(k+1) for _ in range(ALL)]
    DP[0][0] = 0
    for bit in range(1, ALL):
        p_cnt = 0
        for i in range(n):
            if (bit >> i & 1):
                p_cnt += 1
        for group in range(1, min(k, p_cnt)+1):
            sub_bit = bit
            dist_sub = INF
            while sub_bit > 0:
                sub_bit = (sub_bit-1) & bit  # foo & bit で foo以下のbitを内包する最大のbitになる
                r_sub_bit = bit ^ sub_bit  # bit ^ sで集合でいえばbit-sになる
                dist_sub = max(DP[sub_bit][group-1], dist_bit[r_sub_bit])
                DP[bit][group] = min(DP[bit][group], dist_sub)

    print(DP[-1][-1])


main()
