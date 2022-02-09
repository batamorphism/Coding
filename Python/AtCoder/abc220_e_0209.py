# lca別に考える
def main():
    n, d = map(int, input().split())
    MOD = 998244353
    ans = 0
    for lca_d in range(n):
        # lcaから後どれだけの距離まで許容できるか
        max_depth = n-1-lca_d
        lca_cnt = pow(2, lca_d, MOD)
        # root空の距離をlca_dとする
        # lcaがパスの端である場合
        if d <= max_depth:
            lca_is_st = pow(2, (d+1), MOD)
        else:
            lca_is_st = 0
        # lcaがパスの内部に含まれる場合
        # 1 <= le_dep <= min(max_depth, d-1)
        # 1 <= ri_dep <= min(max_depth, d-1)
        # le_dep + ri_dep = d
        # ゆえに、max(1, d-min(max_depth, d-1)) <= le_dep <= min(max_depth, d-1)
        # として、各le, riに対する答えは
        # (2**(le_dep-1) + 2**(ri_dep-1))*2
        # 2*(2**(d-2))
        # 2**(d-1)
        # となる。
        le_max = min(max_depth, d-1)
        le_min = min(max(1, d-le_max), le_max+1)
        lca_is_inter = (le_max - le_min + 1) * pow(2, (d-1), MOD)
        ans += (lca_is_st + lca_is_inter) * lca_cnt
        ans %= MOD
        # print(lca_d, lca_is_st*lca_cnt, lca_is_inter*lca_cnt)
    print(ans)


main()
