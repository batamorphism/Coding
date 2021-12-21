mod = 10**9+7


def main():
    N, Q = map(int, input().split())
    ALL_N = 1 << N
    W_ = [tuple(map(int, input().split())) for _ in range(Q)]
    W = []
    for x, y, z, w in W_:
        W.append((x-1, y-1, z-1, w))
    # 各nのi桁目のbitをorしたものが、wと一致する組み合わせ数
    ans = 1
    for i in range(60):
        i_cnt = 0
        for bit in range(ALL_N):
            w_check = True
            for x, y, z, w_ in W:
                w = (w_ >> i) & 1
                n_list = [x, y, z]
                or_xyz = 0
                for n in n_list:
                    or_xyz |= (bit >> n & 1)
                if or_xyz != w:
                    w_check = False
            if w_check:
                i_cnt += 1
                i_cnt %= mod
        ans *= i_cnt
        ans %= mod

    print(ans)


main()
