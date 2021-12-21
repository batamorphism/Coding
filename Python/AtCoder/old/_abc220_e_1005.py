def main():
    mod = 998244353
    n, d = map(int, input().split())
    # lca毎に処理する
    ans = 0
    for lca_dep in range(n):
        cnt = 0
        # 深さlca_depの頂点の個数
        lca_cnt = pow(2, lca_dep, mod)

        dist_max = n-lca_dep-1
        # lcaから距離dの点の数
        if d <= dist_max:
            cnt += pow(2, d, mod)

        # 左の木の深さがleft
        # 右の木の深さがrightとして
        # left+right = d
        # left <= dist_max
        # right <= dist_max
        # left > 0
        # right > 0
        # を満たす組み合わせ数は
        # 1 <= left <= dist_max
        # and
        # 1 <= d-left <= dist_max
        # -dist_max <= left-d <= -1
        # d-dist_max <= left <= d-1
        # したがって
        # max(d-dist_max, 1) <= left <= min(dist_max, d-1)
        multi = min(dist_max, d-1)+1-max(d-dist_max, 1)
        multi = max(0, multi)
        if d-2 >= 0:  # powの引数にマイナスが入るとRE
            cnt += pow(2, (d-2), mod)*multi
        # cnt += pow(2, (left-1), mod)*pow(2, (right-1), mod)

        cnt = cnt*lca_cnt % mod
        ans = (ans+cnt) % mod
    print(ans*2 % mod)


main()
