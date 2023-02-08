def main():
    a, b = map(int, input().split())
    lo = solve(a-1)
    hi = solve(b)
    ans = (b-a+1)-(hi-lo)
    print(ans)


def solve(n_max):
    # n以下の数値のうち、4, 9が入っていないものの数
    if n_max == 0:
        return 0
    n_list = [int(i) for i in str(n_max)]

    # 桁DP
    # dp = 4と9が入っていない数の個数
    dp = 0
    is_have_49 = False
    for i, n_i in enumerate(n_list):
        new_dp = 0
        # 1. 今までの数値の末尾に0～9を追加
        for val in range(10):
            if val != 4 and val != 9:
                new_dp += dp

        # 2. 新たに1桁の数値を追加
        if i != 0:
            for val in range(1, 10):
                if val != 4 and val != 9:
                    new_dp += 1

        # 3. top_valから連鎖
        if not is_have_49:
            if i == 0:
                val_begin = 1
            else:
                val_begin = 0
            val_end = n_i
            for val in range(val_begin, val_end):
                if val != 4 and val != 9:
                    new_dp += 1

        # 4. top_valの更新
        if n_i == 4 or n_i == 9:
            is_have_49 = True
        dp = new_dp

    # 5. n_maxの処理
    if not is_have_49:
        dp += 1
    return dp


main()
