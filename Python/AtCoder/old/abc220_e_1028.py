mod = 998244353


def main():
    n, d = map(int, input().split())
    # lca毎に組み合わせ数を求める
    ans = 0
    for lca_d in range(n):
        lca_ans = 0  # 各lca毎の組み合わせ数
        lca_num = pow(2, lca_d, mod)  # lcaが何パターンあるか

        # (i, j)のいずれかがlcaそのものである場合
        if n-lca_d-1 >= d:
            lca_ans += pow(2, d, mod)  # (1 << d) % mod

        # (i, j)両方ともlcaでない場合
        # lcaからの左側の深さをle_d, 右側をri_dとする
        # 2**(le_d-1)*2**(ri_d-1)を各le_dに対して合計すれば答え
        # = 2**(le_d+ri_d-2)
        # ここで、le_d+ri_d = dより
        # 2**(d-2)
        # le_dの取りうるパターン数は
        # 1 <= le_d <= min(d-1, n-lca_d-1)
        # かつ
        # 1 <= ri_d <= min(d-1, n-lca_d-1)
        # 1 <= d-le_d <= min(d-1, n-lca_d-1)
        # -min(d-1, n-lca_d-1) <= le_d-d <= -1
        # d-min(d-1, n-lca_d-1) <= le_d <= d-1
        # したがって
        # d-min(d-1, n-lca_d-1) <= le_d <= min(d-1, n-lca_d-1)
        if d-2 >= 0:
            foo = pow(2, d-2, mod)  # (1 << (d-2)) % mod
        else:
            foo = 0
        baa = max((min(d-1, n-lca_d-1)-(d-min(d-1, n-lca_d-1))+1), 0) % mod
        lca_ans += (foo*baa) % mod
        lca_ans *= lca_num
        lca_ans %= mod
        ans += lca_ans
        ans %= mod
    print(ans*2 % mod)


main()