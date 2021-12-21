def main():
    n_end, w_max = map(int, input().split())
    # (value, weight)
    item_list = []
    for _ in range(n_end):
        v, w = map(int, input().split())
        item_list.append((v, w))

    # DP
    # DP[n][w] = n個の荷物まで見た状態で、容量w以下で収まる範囲でのvalueの合計の最大値
    DP = [[0]*(w_max+1) for _ in range(n_end)]
    for n in range(n_end):
        for w in range(w_max+1):
            value, weight = item_list[n]
            if w >= weight:
                add_n_value = DP[n-1][w-weight]+value
            else:
                add_n_value = 0
            not_add_value = DP[n-1][w]
            DP[n][w] = max(add_n_value, not_add_value)
    print(DP[-1][-1])


main()
