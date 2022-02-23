# 桁DP
def main():
    n_list = list(map(int, input()))
    m = int(input())
    C = list(map(int, input().split()))
    mask = 0
    for c_i in C:
        mask |= 1 << c_i
    MOD = 998244353
    ALL = 1 << 10

    # DP[bit] := bitを使用している数値が何通りあるか
    DP = [0] * ALL
    DP_SUM = [0] * ALL
    top_S = 0
    top_val = 0
    is_first = True
    for cur_n in n_list:
        new_DP = [0] * ALL
        new_DP_SUM = [0] * ALL
        # 1. 1~9を追加
        if not is_first:
            for val in range(1, 10):
                new_DP[1 << val] += 1
                new_DP_SUM[1 << val] += val
        # 2. 既にある数値の末尾に数値を追加
        for val in range(10):
            for cur_S in range(ALL):
                nex_S = cur_S | (1 << val)
                new_DP[nex_S] += DP[cur_S]
                new_DP_SUM[nex_S] += DP_SUM[cur_S]*10 + val*DP[cur_S]
        # 3. top_valから派生
        if not is_first:
            val_begin = 0
        else:
            val_begin = 1
        val_end = cur_n
        for val in range(val_begin, val_end):
            # top_val*10 + valを追加
            nex_S = top_S | (1 << val)
            new_DP[nex_S] += 1
            new_DP_SUM[nex_S] += top_val*10 + val

        top_val = (top_val * 10 + cur_n) % MOD
        top_S |= 1 << cur_n
        is_first = False
        for S in range(ALL):
            DP[S] = new_DP[S] % MOD
            DP_SUM[S] = new_DP_SUM[S] % MOD

    # top_valの更新
    DP[top_S] += 1
    DP_SUM[top_S] += top_val
    ans = 0
    for S in range(ALL):
        if S & mask != mask:
            continue
        ans += DP_SUM[S]
        ans %= MOD
    print(ans)


main()
