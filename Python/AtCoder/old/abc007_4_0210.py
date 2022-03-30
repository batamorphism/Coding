def main():
    a, b = map(int, input().split())
    hi = solve(b)
    lo = solve(a-1)
    print((b-a+1) - (hi-lo))


def solve(n_int):
    # n以下の正整数であり、4と9を含まないものの数
    # 0は含めない
    number = [0] + list(map(int, str(n_int)))
    dp = 0
    top_val = 0
    for cur_dgt in range(len(number)-1):
        nex_dgt = cur_dgt + 1
        new_dp = 0
        # 1. 新たに始まる1桁の数
        if cur_dgt >= 1:
            new_dp += 7  # 1235678
        # 2. 既にある数値の末尾に追加
        new_dp += dp*8  # dp*10+(0, ...,8)
        # 3. top_valから連鎖
        if top_val != -1:
            nex_val = number[nex_dgt]
            if cur_dgt == 0:
                val_begin = 1
            else:
                val_begin = 0
            # 1, ..., nex_val-1
            for val in range(val_begin, nex_val):
                if val == 4 or val == 9:
                    continue
                new_dp += 1

        dp = new_dp
        if nex_val == 4 or nex_val == 9:
            top_val = -1
        else:
            top_val = top_val * 10 + nex_val

    # 最後の数
    if top_val != -1 and top_val != 0:
        dp += 1
    return dp


main()
