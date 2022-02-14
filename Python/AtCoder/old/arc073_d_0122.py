# 1番目を見ると
# あるw_loが存在し
# w_lo <= w_i <= w_lo+3である
# したがって、n個選ぶことを固定した場合は、ナップザックDPで解ける
def main():
    n_max, W = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(n_max)]
    w_lo = item_list[0][0]
    item_list = [(0, 0)] + [(w - w_lo, val) for w, val in item_list]
    sum_w = sum(w for w, val in item_list)

    ans = 0
    for n in range(1, n_max+1):
        W_n = min(W - w_lo*n, sum_w)
        if W_n >= 0:
            ans = max(ans, knapsack(item_list, W_n, n))

    print(ans)


def knapsack(item_list, W, n):
    # item_listからn個選び、W以下の重量における価値の最大値
    # DP[i][cnt][w] := i番目を選んだ状態で、既にcnt個選んでおり、w以下の重量における価値の最大値
    DP = [[[0] * (W+1) for _ in range(n+1)] for _ in range(len(item_list))]
    for i in range(1, len(item_list)):
        for cnt in range(1, n+1):
            for w in range(W+1):
                w_i, v_i = item_list[i]
                if w-w_i >= 0:
                    DP[i][cnt][w] = max(DP[i-1][cnt][w], DP[i-1][cnt-1][w-w_i] + v_i)
                else:
                    DP[i][cnt][w] = DP[i-1][cnt][w]

    return DP[-1][-1][-1]


main()
