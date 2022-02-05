def main():
    item_end, w_max = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(item_end)]

    DP = [0] * (w_max + 1)
    # 配るDP
    for cur_w in range(w_max+1):
        cur_v = DP[cur_w]
        for v_i, w_i in item_list:
            nex_v = cur_v + v_i
            nex_w = cur_w + w_i
            if nex_w > w_max:
                continue
            DP[nex_w] = max(DP[nex_w], nex_v)

    ans = max(DP)
    print(ans)


main()
