def main():
    n, m, d, k = map(int, input().split())
    # n頂点、m辺のグラフ
    # nは1000以下、mは3000以下
    # mは
    # d日間、k回の修繕が可能
    edge_list = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge_list.append((u, v, w))

    nei_of = [[] for _ in range(n)]
    for id, (fr, to, cost) in enumerate(edge_list):
        nei_of[fr].append((to, cost, id))
        nei_of[to].append((fr, cost, id))

    # node_list = []  # 各nodeのx, y座標。使わなくてもよい
    for _ in range(n):
        _, _ = map(int, input().split())
        # node_list.append((x, y))

    import time
    st_time = time.time()

    # 全ての辺をちょうど1回ずつ工事したい。
    # 工事すると、その間通行できなくなる
    # 不満度は、各頂点の経路の合計
    # ワーシャルフロイド法（すべて取る）場合、O(n**3)
    # ダイクストラ（ランダムな2点）の場合、O(N+E)

    # 正の得点を得る
    day_of_edge = [0] * m  # 各辺の工事日
    # m個をd個に分ける
    per_day = (m+d+1) // d  # 1日あたりに工事する辺の数
    for edge in range(m):
        day = edge // per_day
        day_of_edge[edge] = day
    # print(*day_of_edge)
    cnt_of_day = [0] * d  # 各日に工事する辺の数
    for day in day_of_edge:
        cnt_of_day[day] += 1

    # 焼きなまし法
    # 1つの辺について、工事する日を変更する。
    # 1. 変更した後の、その日の工事数がkを超えていないかをチェックする。
    # 2. ランダムに頂点のペアを100個選び、ダイクストラで最短経路を求める。
    # 3. 変更前後で不満度が減少していれば採用する。
    import random
    random.seed(0)
    time_limit = 5.5
    while time.time() - st_time < time_limit:
        # ランダムな辺を選択する
        ch_edge = random.randint(0, m-1)
        bef_day = day_of_edge[ch_edge]
        # 1. 変更した後の、その日の工事数がkを超えていないかをチェックする。
        # これは、変更後の日の高次数がk-1以下であるまで、aft_dayをランダムに選び直す。
        aft_day = random.randint(0, d-1)
        while cnt_of_day[aft_day] >= k:
            aft_day = random.randint(0, d-1)
        # 2. ランダムに頂点のペアを10個選び、ダイクストラで最短経路を求める。
        # ただし、工事中の辺については、通行できないとする。
        node_pair_list = []
        for _ in range(10):
            st_node = random.randint(0, n-1)
            en_node = random.randint(0, n-1)
            if st_node == en_node:
                en_node = (en_node + 1) % n
            node_pair_list.append((st_node, en_node))
        bef_score = 0
        for st_node, en_node in node_pair_list:
            # bef_dayとaft_dayだけがスコアが変わるので、この2についてのみ計算する
            bef_score += dijkstra(n, nei_of, st_node, en_node, bef_day, day_of_edge)
            bef_score += dijkstra(n, nei_of, st_node, en_node, aft_day, day_of_edge)

        aft_score = 0
        day_of_edge[ch_edge] = aft_day
        for st_node, en_node in node_pair_list:
            aft_score += dijkstra(n, nei_of, st_node, en_node, bef_day, day_of_edge)
            aft_score += dijkstra(n, nei_of, st_node, en_node, aft_day, day_of_edge)

        if aft_score < bef_score:
            # 採用する
            cnt_of_day[bef_day] -= 1
            cnt_of_day[aft_day] += 1
        else:
            # 変更を取り消す
            day_of_edge[ch_edge] = bef_day

    # 答えを出力する
    ans = []
    for day in day_of_edge:
        ans.append(day+1)
    print(*ans)


def dijkstra(node_end, nei_of, st, en, day, day_of_edge):
    # stからenまでの最短経路を返す
    import heapq
    INF = 10**18
    dist = [INF] * node_end
    dist[st] = 0
    que = []
    heapq.heappush(que, (0, st))
    while que:
        d, fr = heapq.heappop(que)
        if dist[fr] < d:
            continue
        for to, cost, id in nei_of[fr]:
            # 辺：idが工事中の場合、通行できない
            if day == day_of_edge[id]:
                cost = INF
            if dist[to] > dist[fr] + cost:
                dist[to] = dist[fr] + cost
                heapq.heappush(que, (dist[to], to))
    return dist[en]


main()
