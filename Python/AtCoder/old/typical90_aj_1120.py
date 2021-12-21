INF = 10**9


def main():
    n, q = map(int, input().split())
    P = [tuple(map(int, input().split())) for _ in range(n)]
    Q = [int(input())-1 for _ in range(q)]

    # マンハッタン距離は45度回転
    # (1, 1) -> (2, 0)
    # とする。この操作はマンハッタン距離を変えない
    # A = 1 ,1
    #    -1, 1

    aft_P = []
    for x, y in P:
        # 回転
        x, y = x+y, -x+y
        aft_P.append((x, y))

    # x座標y座標の最大値最小値を求める
    max_x = -INF
    min_x = INF
    max_y = -INF
    min_y = INF
    for x, y in aft_P:
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    # 各max, minとの距離を求める
    for query in Q:
        x, y = aft_P[query]
        ans = max(abs(max_x-x), abs(min_x-x), abs(max_y-y), abs(min_y-y))
        print(ans)


main()
