def main():
    n, w_max = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(n)]

    # DP[w] = 重さwで達成しうる価値の合計の最大値
    # 使えるアイテムは一個だけ
    INF = float('inf')
    DP = [-INF]*(w_max+1)
    DP[0] = 0
    # 配るDP
    for v_i, w_i in item_list:
        new_DP = [-INF]*(w_max+1)
        for pre_w in range(w_max+1):
            # i番目のアイテムを使わない場合
            new_DP[pre_w] = max(DP[pre_w], new_DP[pre_w])
            # i番目のアイテムを使う場合
            cur_w = pre_w + w_i
            cur_v = DP[pre_w] + v_i
            if cur_w <= w_max:
                new_DP[cur_w] = max(DP[cur_w], cur_v, new_DP[cur_w])
        DP = new_DP[:]

    ans = max(DP)
    print(ans)


main()
