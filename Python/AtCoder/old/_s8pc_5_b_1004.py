def main():
    # NもMも100以下
    # 組み合わせ数は200*199/2=19,900で十分計算可能
    # 各mに対し、(n+m)に対し考えうる半径の最大値を求める
    # 相手がnの場合、dist(p1, p2)-r1
    # 相手がmの場合、dist(p1, p2)/2
    n, m = map(int, input().split())
    st_ring_list = []
    dy_ring_list = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        st_ring_list.append((x, y, r))
    for _ in range(m):
        x, y = map(int, input().split())
        dy_ring_list.append((x, y))
    ans = 10**10

    if m == 0:
        for p in st_ring_list:
            x, y, r = p
            ans = min(r, ans)
    # 相手がmの場合
    for p1 in dy_ring_list:
        for p2 in dy_ring_list:
            if p1 == p2:
                continue
            ans = min(dist(p1, p2)/2, ans)

    # 相手がnの場合
    for p1 in dy_ring_list:
        for p2_r in st_ring_list:
            x, y, r = p2_r
            p2 = (x, y)
            ans = min(dist(p1, p2)-r, ans)

    print(ans)


def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x1-x2)**2+(y1-y2)**2)**0.5


main()
