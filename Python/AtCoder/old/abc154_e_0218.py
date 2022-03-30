def main():
    number = list(map(int, input()))
    k = int(input())

    # 0でない数がいくつかるか
    DP = [0]*(k+1)
    top_val = 0
    top_cnt = 0  # top_valに0でない数値がいくつあるか
    for cur_dgt, cur_num in enumerate(number):
        nex_DP = [0]*(k+1)
        # 1桁の数字
        if cur_dgt != 0:
            # 1~9を足す
            nex_DP[1] += 9

        # 既にある数値の末尾に足す
        for cur_cnt in range(k+1):
            nex_cnt = cur_cnt + 1
            nex_DP[cur_cnt] += DP[cur_cnt]  # 0を追加
            if nex_cnt <= k:
                nex_DP[nex_cnt] += DP[cur_cnt]*9  # 1~9を追加

        # top_valから連鎖
        if top_val == 0:
            nex_val_begin = 1
            nex_val_end = cur_num
        else:
            nex_val_begin = 0
            nex_val_end = cur_num
        for nex_val in range(nex_val_begin, nex_val_end):
            if nex_val == 0:
                nex_cnt = top_cnt
            else:
                nex_cnt = top_cnt + 1
            if nex_cnt <= k:
                nex_DP[nex_cnt] += 1

        top_val = 1
        if cur_num != 0:
            top_cnt += 1
        for cnt in range(1, k+1):
            DP[cnt] = nex_DP[cnt]

    # top_valを足す
    if top_cnt <= k:
        DP[top_cnt] += 1

    ans = DP[k]
    print(ans)


main()
