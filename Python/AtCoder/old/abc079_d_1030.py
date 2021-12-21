INF = 10**9


def main():
    r_end, c_end = map(int, input().split())
    cost = []
    for _ in range(10):
        c = list(map(int, input().split()))
        cost.append(c)
    A = [list(map(int, input().split())) for _ in range(r_end)]

    # ワーシャルフロイド
    dist = [[INF]*10 for _ in range(10)]
    for k in range(10):
        for fr in range(10):
            for to in range(10):
                # frからtoにかけて、0～kだけを使った場合の最短距離
                direct = cost[fr][to]
                not_use_k = dist[fr][to]
                use_k = dist[fr][k]+dist[k][to]
                dist[fr][to] = min(direct, not_use_k, use_k)

    ans = 0
    for row in A:
        for a in row:
            if a != -1:
                ans += dist[a][1]
    print(ans)


main()
