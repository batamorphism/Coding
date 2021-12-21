# 0~n-1のn個の都市
# 0~m-1のm個の鉄道
# 鉄道はaとbをつないでいる
# この列車はtの時間がかかる

import heapq


def main():
    # input
    n, m, x, y = map(int, input().split())
    A = []
    B = []
    T = []
    K = []
    for _ in range(m):
        a, b, t, k = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
        T.append(t)
        K.append(k)

    # init
    # 各都市の鉄道の情報を入れる
    graph = [[] for _ in range(n)]
    for i in range(m):
        graph[A[i]].append((B[i], T[i], K[i]))
        graph[B[i]].append((A[i], T[i], K[i]))

    mindist = [10**20] * n  # 各都市の最短距離
    fixed = [False] * n  # 最短距離になったか、つまり探索済みか
    hq = []
    heapq.heappush(hq, (0, x-1))    # 都市xからスタート、コスト,nodeの順にしておくこと

    while hq:
        dist, node = heapq.heappop(hq)  # heapqなので、コスト順に処理される
        if fixed[node]:  # 探索済みの頂点は無視する
            continue
        fixed[node] = True
        for i, t, k in graph[node]:
            if next_cost(dist, k, t) >= mindist[i]:
                continue
            heapq.heappush(hq, (next_cost(dist, k, t), i))
            mindist[i] = next_cost(dist, k, t)  # 暫定の距離を入れていく

        # 枝刈り拘束化
        if node == y-1:
            break

    if fixed[y-1]:
        print(mindist[y-1])
    else:
        print(-1)


def divceil(n, k):
    return 1+(n-1)//k


def next_cost(dist, k, t):
    return divceil(dist, k)*k+t


main()
