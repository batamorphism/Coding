# DP[w] = 重さがwである時の、価値の最大値
def main():
    # 容量W
    item_end, w_max = map(int, input().split())
    item_list = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(item_end)]

    # DPは1-indexed
    item_end += 1
    DP = [0]*(w_max+1)

    # 初期値は、DP[0][0] = 0

    # 配るDP
    for cur_w in range(w_max+1):
        cur_v = DP[cur_w]
        for item_v, item_w in item_list:
            nex_v = cur_v + item_v
            nex_w = cur_w + item_w
            if nex_w > w_max:
                continue
            DP[nex_w] = max(DP[nex_w], nex_v)

    ans = DP[-1]
    print(ans)


main()
