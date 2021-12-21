# 木の距離はLCA
# 木の深さを1～nとする。
# 深さlca_dのlca毎に処理する
# 深さlca_dのlcaは、2**(d-1)個存在
# lcaから葉までの距離leaf_dはn-lca_d
# (i, j)について、iかjがlcaである場合、leaf_d >= dの場合に限り2**d個存在

# (i, j)について、iかjがlcaでない場合、
# iがlcaのle, jがlcaのriとして、le = i, ri = jと置く
# lcaからの距離をle_d, ri_dとして
# le_d = 1, ...,d-1 (ただし上限はleaf_d)
# ri_d = d-1, ...,1
# したがってmax_le_d = min(d-1, leaf_d)として
# min_le_d = d-max_le_dとなり
# le_d = min_le_d, ...,max_le_d
# それぞれについて、leは2**(le_d-1)個存在
# riは2**(ri_d-1)個存在
# 合わせて、2**(le_d+ri_d-2)個存在
# le_d+ri_d = dより
# 2**(d-2)*(max_le_d - min_le_d + 1)
# 最後に、le, riの対称性から2倍
mod = 998244353


def main():
    n, d = map(int, input().split())
    ans = 0
    for lca_d in range(1, n+1):
        leaf_d = n-lca_d
        if leaf_d <= 0:
            break
        # lca_d_cnt = 2**(lca_d-1)
        lca_d_cnt = pow(2, (lca_d-1), mod)
        ans_of_lca = 0  # 最後lca_cnt倍する前提の答え
        if leaf_d >= d:
            # ans_of_lca += 2**d*2
            ans_of_lca += pow(2, d, mod)*2
        max_le_d = min(d-1, leaf_d)
        min_le_d = d-max_le_d
        # ans_of_lca += 2**(d-2)*(max_le_d - min_le_d + 1)*2
        if d-2 >= 0:
            if max_le_d >= min_le_d:
                ans_of_lca += pow(2, (d-2), mod)*(max_le_d - min_le_d + 1)*2
        # print(lca_d, lca_d_cnt, ans_of_lca)
        ans += ans_of_lca*lca_d_cnt
        ans %= mod

    print(ans)


main()
