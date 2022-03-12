# 同じ種類の品物はいくつでも選べる
def main():
    item_end, w_max = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(item_end)]

    DP = [0] * (w_max + 1)
    # 配るDP
    for pre_w in range(w_max):
        pre_v = DP[pre_w]
        for v_i, w_i in item_list:
            cur_w = pre_w + w_i
            cur_v = pre_v + v_i
            if cur_w > w_max:
                continue
            DP[cur_w] = max(DP[cur_w], cur_v)

    ans = max(DP)
    print(ans)


main()
