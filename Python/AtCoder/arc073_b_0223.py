def main():
    item_end, weight_max = map(int, input().split())
    dp = {0: 0}  # dp[weight] = value
    # wは重複しまくるので、間に合う
    item_list = [tuple(map(int, input().split())) for _ in range(item_end)]

    for wei, val in item_list:
        cur_dp = dp.copy()
        for cur_wei, cur_val in cur_dp.items():
            nex_wei = cur_wei + wei
            nex_val = cur_val + val
            if nex_wei > weight_max:
                continue
            dp[nex_wei] = max(dp.get(nex_wei, 0), nex_val)

    ans = max(dp.values())
    print(ans)


main()
