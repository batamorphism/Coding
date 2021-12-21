INF = 10**9


def main():
    # n, mの組み合わせ全探索
    n, m = map(int, input().split())
    n_list = []
    m_list = []
    ans = INF
    for _ in range(n):
        x, y, r = map(int, input().split())
        n_list.append((x, y, r))
        ans = min(ans, r)
    for _ in range(m):
        x, y = map(int, input().split())
        m_list.append((x, y))

    for c1_ind in range(m):
        c1_x, c1_y = m_list[c1_ind]
        for c2_ind in range(m):
            if c1_ind == c2_ind:
                continue
            c2_x, c2_y = m_list[c2_ind]
            # c1とc2の距離の1/2で更新
            d = ((c1_x - c2_x)**2 + (c1_y - c2_y)**2)**0.5
            d /= 2
            ans = min(ans, d)
        for c2_ind in range(n):
            c2_x, c2_y, c2_r = n_list[c2_ind]
            # c1とc2の距離-rで更新
            d = ((c1_x - c2_x)**2 + (c1_y - c2_y)**2)**0.5
            d -= c2_r
            ans = min(ans, d)

    print(ans)


main()
