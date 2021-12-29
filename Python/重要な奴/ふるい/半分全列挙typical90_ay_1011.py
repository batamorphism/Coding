# https://atcoder.jp/contests/typical90/submissions/26493244
def main():
    # 半分全列挙
    n, k, p = map(int, input().split())
    A = list(map(int, input().split()))
    sep = (n-1)//2+1
    A_l = A[:sep]
    A_r = A[sep:]
    sum_list_l_of_k = [[] for _ in range(n+1)]  # 左側の、商品の個数ごとに、価格の合計値として取りうる値
    sum_list_r_of_k = [[] for _ in range(n+1)]
    set_sum_list_of(A_l, sum_list_l_of_k)
    set_sum_list_of(A_r, sum_list_r_of_k)

    ans = 0
    for k_l, sum_list_l in enumerate(sum_list_l_of_k):
        k_r = k-k_l
        sum_list_r = sum_list_r_of_k[k_r]
        for sum_l in sum_list_l:
            sum_r_max = p - sum_l
            # sum_r_maxを下回るsum_list_rの要素数を調べる
            ok = -1
            ng = len(sum_list_r)
            while ng-ok > 1:
                mid = (ok+ng)//2
                if sum_list_r[mid] <= sum_r_max:
                    ok = mid
                else:
                    ng = mid
            ans += ok+1

    print(ans)


def set_sum_list_of(A: list, sum_list_of: list):
    n = len(A)
    All = 1 << n
    for bit in range(All):
        sum = 0
        cnt = 0
        for i in range(n):
            if bit >> i & 1:
                sum += A[i]
                cnt += 1
        sum_list_of[cnt].append(sum)
    # sort
    for k in range(len(sum_list_of)):
        sum_list_of[k].sort()
    return


main()
