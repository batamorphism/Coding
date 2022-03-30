def main():
    n, s = map(int, input().split())
    # DP[val] = val円となる買い方が存在する
    DP = [False]*(s+1)
    DP[0] = True
    # par[val] = 合計val円を買うとなった時の、買う前の合計金額と買ったアイテム
    par = [(-1, -1) for _ in range(s+1)]

    item_list = []
    for _ in range(n):
        a, b = map(int, input().split())
        item_list.append((a, b))

    DP_list = []
    DP_list.append(DP[:])
    par_list = []
    par_list.append(par[:])

    # DP
    for a, b in item_list:
        new_DP = [False]*(s+1)
        par = [(-1, -1) for _ in range(s+1)]
        for pre_val in reversed(range(s+1)):
            if not DP[pre_val]:
                continue
            # a_side
            cur_val = pre_val + a
            if cur_val <= s:
                new_DP[cur_val] = True
                par[cur_val] = (pre_val, 'A')
            # b_side
            cur_val = pre_val + b
            if cur_val <= s:
                new_DP[cur_val] = True
                par[cur_val] = (pre_val, 'B')
        DP = new_DP[:]
        DP_list.append(DP[:])
        par_list.append(par[:])

    if not DP[s]:
        print('Impossible')
        return

    # DP復元
    ans = []
    cur_val = s
    for day in reversed(range(n)):
        par = par_list[day+1]
        pre_val, item = par[cur_val]
        ans.append(item)
        cur_val = pre_val
    if cur_val != 0:
        raise
    ans = ans[::-1]
    print(''.join(ans))


main()
