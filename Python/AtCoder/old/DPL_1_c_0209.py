# 同じものを何度も選べるナップザックDP
def main():
    item_end, w_max = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(item_end)]

    DP = [0]*(w_max+1)

    for cur_w, cur_dp in enumerate(DP):
        for v_i, w_i in item_list:
            nex_w = cur_w + w_i
            nex_dp = cur_dp + v_i
            if nex_w <= w_max:
                DP[nex_w] = max(DP[nex_w], nex_dp)

    ans = max(DP)
    print(ans)


main()
